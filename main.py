import sys
import fitz  # PyMuPDF
import re
import phonenumbers
import spacy
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFileDialog, 
                             QCheckBox, QGroupBox, QFormLayout, QSpacerItem, QSizePolicy, QTabWidget, QScrollArea, QProgressBar, QStackedWidget, QSplitter, QRadioButton)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPropertyAnimation, QRect, QTimer
from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap, QImage
import os
import time

# İngilizce NER modelini yükleme
try:
    nlp_en = spacy.load("en_core_web_sm")
except OSError:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp_en = spacy.load("en_core_web_sm")

# Regex kalıpları
email_regex = re.compile(
    r'''(?i)\b(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+
    (?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*
    |"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]
    |\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")
    @(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+
    [a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[
    (?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).
    ){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|
    [a-z0-9-]*[a-z0-9]:
    (?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]
    |\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''', re.VERBOSE)

phone_regex = re.compile(
    r'(\+?\d{1,3}[-.\s]?)?'      # Ülke kodu (isteğe bağlı)
    r'(\(?\d{3}\)?[-.\s]?)?'    # Alan kodu (isteğe bağlı)
    r'\d{3}[-.\s]?\d{4}'         # Ana numara
)

class MaskingThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, pdf_path, output_path, options):
        super().__init__()
        self.pdf_path = pdf_path
        self.output_path = output_path
        self.options = options

    def run(self):
        mask_sensitive_information(self.pdf_path, self.output_path, **self.options)
        self.finished.emit(self.output_path)

class PDFMaskApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Masking Tool")
        self.setGeometry(100, 100, 1200, 800)
        
        # Modern bir tema ayarlama
        self.setStyleSheet("""
            QWidget {
                font-size: 14px;
                background-color: #2e2e2e;
                color: #ffffff;
            }
            QPushButton {
                background-color: #5A9;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #4A8;
            }
            QLabel {
                font-weight: bold;
                color: #ffffff;
            }
            QCheckBox {
                margin: 5px;
            }
            QGroupBox {
                border: 1px solid #666;
                border-radius: 5px;
                margin-top: 10px;
                background-color: #3e3e3e;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 3px;
                background-color: #4e4e4e;
            }
            QRadioButton {
                margin: 5px;
            }
        """)
        
        # Main layout with splitter
        self.splitter = QSplitter(Qt.Horizontal)
        self.setCentralWidget(self.splitter)
        
        # Sidebar for options
        self.sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout()
        self.sidebar_widget.setLayout(sidebar_layout)
        
        # PDF Selection
        self.pdf_path_label = QLabel("No PDF Selected")
        self.pdf_path_label.setAlignment(Qt.AlignCenter)
        select_pdf_btn = QPushButton("Select PDF")
        select_pdf_btn.clicked.connect(self.select_pdf)
        
        sidebar_layout.addWidget(self.pdf_path_label)
        sidebar_layout.addWidget(select_pdf_btn)
        
        # Masking Options
        masking_group = QGroupBox("Masking Options")
        masking_layout = QVBoxLayout()
        masking_group.setLayout(masking_layout)
        
        self.mask_email_checkbox = QCheckBox("Mask Email")
        self.mask_phone_checkbox = QCheckBox("Mask Phone Number")
        self.mask_address_checkbox = QCheckBox("Mask Address")
        
        masking_layout.addWidget(self.mask_email_checkbox)
        masking_layout.addWidget(self.mask_phone_checkbox)
        masking_layout.addWidget(self.mask_address_checkbox)
        
        sidebar_layout.addWidget(masking_group)
        
        # Entity Selection
        entity_group = QGroupBox("Select Entities to Mask")
        entity_layout = QFormLayout()
        self.mask_person_checkbox = QCheckBox("Mask Person")
        self.mask_gpe_checkbox = QCheckBox("Mask GPE")
        self.mask_loc_checkbox = QCheckBox("Mask Location")
        self.mask_org_checkbox = QCheckBox("Mask Organization")
        
        entity_layout.addRow(self.mask_person_checkbox)
        entity_layout.addRow(self.mask_gpe_checkbox)
        entity_layout.addRow(self.mask_loc_checkbox)
        entity_layout.addRow(self.mask_org_checkbox)
        entity_group.setLayout(entity_layout)
        
        sidebar_layout.addWidget(entity_group)
        
        # Masking Style Options
        style_group = QGroupBox("Masking Style")
        style_layout = QVBoxLayout()
        style_group.setLayout(style_layout)
        
        self.style_star_radio = QRadioButton("Mask with *")
        self.style_black_radio = QRadioButton("Blackout")
        self.style_frame_radio = QRadioButton("Frame")
        
        self.style_star_radio.setChecked(True)  # Varsayılan olarak * ile maskeleme
        
        style_layout.addWidget(self.style_star_radio)
        style_layout.addWidget(self.style_black_radio)
        style_layout.addWidget(self.style_frame_radio)
        
        sidebar_layout.addWidget(style_group)
        
        # Mask PDF Button
        mask_pdf_btn = QPushButton("Mask PDF")
        mask_pdf_btn.clicked.connect(self.start_masking)
        sidebar_layout.addWidget(mask_pdf_btn)
        
        # Loading Indicator
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate state
        self.progress_bar.setVisible(False)
        sidebar_layout.addWidget(self.progress_bar)
        
        # Add sidebar to splitter
        self.splitter.addWidget(self.sidebar_widget)
        
        # PDF Preview Area
        preview_widget = QWidget()
        preview_layout = QVBoxLayout()
        preview_widget.setLayout(preview_layout)
        
        self.preview_tabs = QTabWidget()
        self.original_preview = QStackedWidget()
        self.masked_preview = QStackedWidget()
        
        self.preview_tabs.addTab(self.original_preview, "Original PDF")
        self.preview_tabs.addTab(self.masked_preview, "Masked PDF")
        
        preview_layout.addWidget(self.preview_tabs)
        self.splitter.addWidget(preview_widget)
        
        # Sidebar için maksimum genişlik ayarlama
        self.sidebar_widget.setMaximumWidth(250)  # Biraz daha geniş

        # Sayfa numarası göstermek için QLabel
        self.page_number_label = QLabel("", self)
        self.page_number_label.setStyleSheet("font-size: 16px; color: #ffffff; background-color: rgba(0, 0, 0, 0.5);")
        self.page_number_label.setAlignment(Qt.AlignCenter)
        self.page_number_label.setVisible(False)
        preview_layout.addWidget(self.page_number_label)

        # Sayfalar arası gezinme butonları
        navigation_layout = QHBoxLayout()
        prev_page_btn = QPushButton("Previous Page")
        next_page_btn = QPushButton("Next Page")
        prev_page_btn.clicked.connect(lambda: self.change_page(-1))
        next_page_btn.clicked.connect(lambda: self.change_page(1))
        
        navigation_layout.addWidget(prev_page_btn)
        navigation_layout.addWidget(next_page_btn)
        preview_layout.addLayout(navigation_layout)

    def select_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PDF", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdf_path_label.setText(file_path)
            self.show_pdf_preview(file_path, self.original_preview)
    
    def start_masking(self):
        pdf_path = self.pdf_path_label.text()
        if not pdf_path or pdf_path == "No PDF Selected":
            return
        
        # Benzersiz bir dosya adı oluştur
        timestamp = int(time.time())
        self.masked_pdf_path = f"{pdf_path.replace('.pdf', '')}_masked_{timestamp}.pdf"
        
        options = {
            'mask_email': self.mask_email_checkbox.isChecked(),
            'mask_phone': self.mask_phone_checkbox.isChecked(),
            'mask_address': self.mask_address_checkbox.isChecked(),
            'mask_person': self.mask_person_checkbox.isChecked(),
            'mask_gpe': self.mask_gpe_checkbox.isChecked(),
            'mask_loc': self.mask_loc_checkbox.isChecked(),
            'mask_org': self.mask_org_checkbox.isChecked(),
            'style_star': self.style_star_radio.isChecked(),
            'style_black': self.style_black_radio.isChecked(),
            'style_frame': self.style_frame_radio.isChecked()
        }
        
        self.progress_bar.setVisible(True)
        self.masking_thread = MaskingThread(pdf_path, self.masked_pdf_path, options)
        self.masking_thread.finished.connect(self.on_masking_finished)
        self.masking_thread.start()
    
    def on_masking_finished(self, output_path):
        self.progress_bar.setVisible(False)
        
        # PDF dosya yolunu sakla
        pdf_path = output_path  # Çıktı dosya yolunu kullanıyoruz
        
        # PDF önizlemesini göster
        self.show_pdf_preview(pdf_path, self.masked_preview)
        
        # Sol kısmı küçültme animasyonu
        animation = QPropertyAnimation(self.sidebar_widget, b"maximumWidth")
        animation.setDuration(500)
        animation.setStartValue(self.sidebar_widget.width())
        animation.setEndValue(100)  # 100 piksele küçült
        animation.start()
        
        # Maskeleme tamamlandı mesajı göster
        self.pdf_path_label.setText("Maskeleme Tamamlandı")
    
    def show_pdf_preview(self, pdf_path, stacked_widget):
        doc = fitz.open(pdf_path)
        
        # Clear all widgets from the stacked widget
        while stacked_widget.count() > 0:
            widget = stacked_widget.widget(0)
            stacked_widget.removeWidget(widget)
            widget.deleteLater()
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            
            page_label = QLabel()
            page_label.setPixmap(pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            page_label.setAlignment(Qt.AlignCenter)  # Ortala
            
            scroll_area = QScrollArea()
            scroll_area.setWidget(page_label)
            scroll_area.setWidgetResizable(True)
            scroll_area.verticalScrollBar().valueChanged.connect(lambda: self.show_page_number(page_num + 1))
            
            stacked_widget.addWidget(scroll_area)
        
        doc.close()

    def show_page_number(self, page_number):
        self.page_number_label.setText(f"Page {page_number}")
        self.page_number_label.setVisible(True)
        QTimer.singleShot(2000, lambda: self.page_number_label.setVisible(False))  # 2 saniye sonra gizle

    def change_page(self, direction):
        current_index = self.preview_tabs.currentWidget().currentIndex()
        new_index = current_index + direction
        if 0 <= new_index < self.preview_tabs.currentWidget().count():
            self.preview_tabs.currentWidget().setCurrentIndex(new_index)
    
    def download_pdf(self, file_path):
        if file_path and os.path.exists(file_path):
            save_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", file_path, "PDF Files (*.pdf)")
            if save_path:
                try:
                    with open(file_path, 'rb') as f_src:
                        with open(save_path, 'wb') as f_dst:
                            f_dst.write(f_src.read())
                    print(f"File successfully saved to {save_path}")
                except Exception as e:
                    print(f"Error saving file: {e}")

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def highlight_text_in_pdf(self):
        # PDF üzerinde metin vurgulama işlemi
        pass

def mask_sensitive_information(pdf_path, output_path, mask_email=False, mask_phone=False, mask_address=False, mask_person=False, mask_gpe=False, mask_loc=False, mask_org=False, style_star=False, style_black=False, style_frame=False):
    try:
        doc = fitz.open(pdf_path)
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            blocks = page.get_text("dict")["blocks"]
            
            redaction_areas = []
            
            for block in blocks:
                if block['type'] != 0:
                    continue
                
                for line in block["lines"]:
                    for span in line["spans"]:
                        span_text = span["text"]
                        span_bbox = span["bbox"]
                        
                        if mask_email:
                            for match in email_regex.finditer(span_text):
                                match_start, match_end = match.span()
                                char_width = (span_bbox[2] - span_bbox[0]) / len(span_text)
                                match_x0 = span_bbox[0] + match_start * char_width
                                match_x1 = span_bbox[0] + match_end * char_width
                                match_rect = fitz.Rect(match_x0, span_bbox[1], match_x1, span_bbox[3])
                                redaction_areas.append((match_rect, match_end - match_start))
                        
                        if mask_phone:
                            for match in phonenumbers.PhoneNumberMatcher(span_text, None):
                                match_start, match_end = match.start, match.end
                                if phonenumbers.is_valid_number(match.number):
                                    char_width = (span_bbox[2] - span_bbox[0]) / len(span_text)
                                    match_x0 = span_bbox[0] + match_start * char_width
                                    match_x1 = span_bbox[0] + match_end * char_width
                                    match_rect = fitz.Rect(match_x0, span_bbox[1], match_x1, span_bbox[3])
                                    redaction_areas.append((match_rect, match_end - match_start))
                        
                        if mask_address or mask_person or mask_gpe or mask_loc or mask_org:
                            doc_spacy = nlp_en(span_text)
                            for ent in doc_spacy.ents:
                                if ((mask_person and ent.label_ == 'PERSON') or
                                    (mask_gpe and ent.label_ == 'GPE') or
                                    (mask_loc and ent.label_ == 'LOC') or
                                    (mask_org and ent.label_ == 'ORG')):
                                    ent_start, ent_end = ent.start_char, ent.end_char
                                    if ent_end - ent_start > 1:
                                        char_width = (span_bbox[2] - span_bbox[0]) / len(span_text)
                                        ent_x0 = span_bbox[0] + ent_start * char_width
                                        ent_x1 = span_bbox[0] + ent_end * char_width
                                        ent_rect = fitz.Rect(ent_x0, span_bbox[1], ent_x1, span_bbox[3])
                                        redaction_areas.append((ent_rect, ent_end - ent_start))
            
            for rect, length in redaction_areas:
                # Redaksiyon annotasyonu ekle
                if style_black:  # Siyah dolgu ile maskeleme
                    page.add_redact_annot(rect, fill=(0, 0, 0))  # Siyah dolgu rengi
                elif style_frame:  # Çerçeve ile maskeleme
                    page.draw_rect(rect, color=(1, 0, 0), width=1)  # Kırmızı çerçeve
                elif style_star:  # Yıldız ile maskeleme
                    # Yıldız sayısını belirle (yaklaşık olarak)
                    rect_width = rect.width
                    num_stars = max(int(rect_width / 10), 1)  # 10 piksel başına 1 yıldız
                    masked_text = '*' * num_stars
                    
                    # Yıldızları eklemek için uygun pozisyon
                    insert_x = rect.x0
                    insert_y = rect.y1 - (rect.height * 0.2)  # Y pozisyonunu ayarlayın
                    
                    # Orijinal metni gizle
                    page.add_redact_annot(rect, fill=(0, 0, 0))  # Siyah dolgu rengi
                    # Yıldızları ekle
                    page.insert_text(
                        fitz.Point(insert_x, insert_y),
                        masked_text,
                        fontsize=12,  # Orijinal metnin boyutuna göre ayarlayın
                        fontname="helv",  # Helvetica fontunu kullanıyoruz
                        color=(0, 0, 0),
                        overlay=True
                    )

            # Redaksiyonları uygula
            page.apply_redactions()
        
        doc.save(output_path)
        print(f"Document saved to {output_path}")
        doc.close()
    except Exception as e:
        print(f"Error during masking: {e}")

def main():
    app = QApplication(sys.argv)
    window = PDFMaskApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()