import re
import fitz  # PyMuPDF

class PDFMasker:
    @staticmethod
    def mask_tc_number(text):
        # Turkish Identification Number (11 digits)
        return re.sub(r'\b\d{11}\b', 'XXXX-XXXX-XXXX', text)
    
    @staticmethod
    def mask_phone_number(text):
        # Matches various phone number formats
        return re.sub(r'\b(\+\d{1,2}\s?)?(\d{3}[-.]?)?\d{3}[-.]?\d{4}\b', 'XXX-XXX-XXXX', text)
    
    @staticmethod
    def mask_email(text):
        # Email masking
        return re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'XXXX@XXXX.com', text)
    
    @staticmethod
    def mask_address(text):
        # Simple address masking (can be enhanced)
        return re.sub(r'\d+\s+[A-Za-z\s]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd)', 'XXXX Street', text)
    
    @classmethod
    def mask_pdf(cls, input_path, output_path, mask_options):
        doc = fitz.open(input_path)
        
        for page in doc:
            text = page.get_text()
            
            if mask_options.get('tc', False):
                text = cls.mask_tc_number(text)
            if mask_options.get('phone', False):
                text = cls.mask_phone_number(text)
            if mask_options.get('email', False):
                text = cls.mask_email(text)
            if mask_options.get('address', False):
                text = cls.mask_address(text)
            
            page.set_text(text)
        
        doc.save(output_path)
        doc.close()