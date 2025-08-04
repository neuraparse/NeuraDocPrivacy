# NeuraDocPrivacy

A sophisticated PDF document privacy masking tool that uses advanced Natural Language Processing (NLP) and pattern recognition to automatically detect and mask sensitive information in PDF documents.

## 🚀 Features

- **Intelligent Text Detection**: Uses spaCy NLP models to identify named entities
- **Multiple Masking Options**: 
  - Email addresses
  - Phone numbers
  - Personal names
  - Addresses
  - Organizations
  - Geographic locations
- **Flexible Masking Styles**:
  - Star masking (***)
  - Black box masking
  - Frame masking
- **Modern GUI**: Built with PyQt5 for a professional user experience
- **Real-time Preview**: View PDF pages before and after masking
- **Batch Processing**: Process multiple documents efficiently
- **Cross-platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.7+
- PyQt5
- PyMuPDF (fitz)
- spaCy with English language model
- Additional dependencies listed in `requirements.txt`

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/neuraparse/NeuraDocPrivacy.git
   cd NeuraDocPrivacy
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy English model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## 🎯 Usage

### GUI Application

Run the main application:
```bash
python main.py
```

### Command Line Interface

For batch processing or automation:
```bash
python pdf_masker.py --input input.pdf --output output.pdf --mask-email --mask-phone
```

## 🔧 Configuration

The application supports various masking options:

- `--mask-email`: Mask email addresses
- `--mask-phone`: Mask phone numbers  
- `--mask-person`: Mask personal names
- `--mask-address`: Mask addresses
- `--mask-org`: Mask organization names
- `--mask-gpe`: Mask geographic and political entities
- `--mask-loc`: Mask location names

Masking styles:
- `--style-star`: Use asterisk masking (***)
- `--style-black`: Use black box masking
- `--style-frame`: Use frame masking

## 📁 Project Structure

```
NeuraDocPrivacy/
├── main.py              # Main GUI application
├── pdf_masker.py        # Core masking functionality
├── requirements.txt     # Python dependencies
├── main.spec           # PyInstaller specification
├── README.md           # This file
├── .gitignore          # Git ignore rules
└── dist/               # Build output (ignored by git)
```

## 🔒 Privacy & Security

- All processing is done locally on your machine
- No data is sent to external servers
- Original files remain unchanged
- Masked documents are saved as new files

## 🚀 Building Executable

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller main.spec
```

The executable will be created in the `dist/` directory.

## 🧪 Testing

Run tests locally:
```bash
pytest tests/
```

Run with coverage:
```bash
pytest tests/ --cov=. --cov-report=html
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Large PDF files may take longer to process
- Some complex layouts might not mask perfectly
- OCR-processed PDFs may have limited accuracy

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/neuraparse/NeuraDocPrivacy/issues) page
2. Create a new issue with detailed information
3. Include your operating system and Python version

## 🔄 Version History

- **v1.0.0**: Initial release with basic masking functionality
- **v1.1.0**: Added GUI interface and improved NLP detection
- **v1.2.0**: Enhanced masking styles and batch processing

## 🙏 Acknowledgments

- [spaCy](https://spacy.io/) for NLP capabilities
- [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF processing
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) for GUI framework

---

**Note**: This tool is designed for legitimate privacy protection purposes. Please ensure you have proper authorization before processing any documents. 