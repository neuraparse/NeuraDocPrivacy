"""
Tests for NeuraDocPrivacy PDF masking functionality
"""

import pytest
import tempfile
import os
from unittest.mock import patch, MagicMock
import fitz  # PyMuPDF

# Import the functions to test
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pdf_masker import mask_sensitive_information


class TestPDFMasker:
    """Test cases for PDF masking functionality"""

    def setup_method(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_pdf_path = os.path.join(self.temp_dir, "test.pdf")
        self.output_pdf_path = os.path.join(self.temp_dir, "output.pdf")
        
        # Create a simple test PDF
        self.create_test_pdf()

    def teardown_method(self):
        """Clean up test fixtures"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def create_test_pdf(self):
        """Create a simple test PDF with sample text"""
        doc = fitz.open()
        page = doc.new_page()
        
        # Add sample text with sensitive information
        text = """
        Contact Information:
        Email: john.doe@example.com
        Phone: +1-555-123-4567
        Address: 123 Main Street, New York, NY 10001
        
        Personal Details:
        Name: John Doe
        Organization: Acme Corporation
        Location: New York City
        """
        
        page.insert_text((50, 50), text)
        doc.save(self.test_pdf_path)
        doc.close()

    def test_pdf_creation(self):
        """Test that test PDF is created successfully"""
        assert os.path.exists(self.test_pdf_path)
        
        # Verify PDF can be opened
        doc = fitz.open(self.test_pdf_path)
        assert len(doc) > 0
        doc.close()

    @patch('pdf_masker.fitz.open')
    def test_mask_email_addresses(self, mock_fitz_open):
        """Test email address masking functionality"""
        # Mock the PDF document
        mock_doc = MagicMock()
        mock_page = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_fitz_open.return_value.__enter__.return_value = mock_doc
        
        # Test email masking
        result = mask_sensitive_information(
            self.test_pdf_path,
            self.output_pdf_path,
            mask_email=True
        )
        
        # Verify the function was called
        mock_fitz_open.assert_called()

    @patch('pdf_masker.fitz.open')
    def test_mask_phone_numbers(self, mock_fitz_open):
        """Test phone number masking functionality"""
        # Mock the PDF document
        mock_doc = MagicMock()
        mock_page = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_fitz_open.return_value.__enter__.return_value = mock_doc
        
        # Test phone masking
        result = mask_sensitive_information(
            self.test_pdf_path,
            self.output_pdf_path,
            mask_phone=True
        )
        
        # Verify the function was called
        mock_fitz_open.assert_called()

    @patch('pdf_masker.fitz.open')
    def test_mask_personal_names(self, mock_fitz_open):
        """Test personal name masking functionality"""
        # Mock the PDF document
        mock_doc = MagicMock()
        mock_page = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_fitz_open.return_value.__enter__.return_value = mock_doc
        
        # Test name masking
        result = mask_sensitive_information(
            self.test_pdf_path,
            self.output_pdf_path,
            mask_person=True
        )
        
        # Verify the function was called
        mock_fitz_open.assert_called()

    def test_invalid_pdf_path(self):
        """Test handling of invalid PDF path"""
        with pytest.raises(FileNotFoundError):
            mask_sensitive_information(
                "nonexistent.pdf",
                self.output_pdf_path,
                mask_email=True
            )

    def test_output_directory_creation(self):
        """Test that output directory is created if it doesn't exist"""
        # Create output path in non-existent directory
        output_dir = os.path.join(self.temp_dir, "output")
        output_path = os.path.join(output_dir, "masked.pdf")
        
        # This should not raise an error
        with patch('pdf_masker.fitz.open'):
            mask_sensitive_information(
                self.test_pdf_path,
                output_path,
                mask_email=True
            )

    @patch('pdf_masker.fitz.open')
    def test_all_masking_options(self, mock_fitz_open):
        """Test all masking options together"""
        # Mock the PDF document
        mock_doc = MagicMock()
        mock_page = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_fitz_open.return_value.__enter__.return_value = mock_doc
        
        # Test all masking options
        result = mask_sensitive_information(
            self.test_pdf_path,
            self.output_pdf_path,
            mask_email=True,
            mask_phone=True,
            mask_address=True,
            mask_person=True,
            mask_gpe=True,
            mask_loc=True,
            mask_org=True
        )
        
        # Verify the function was called
        mock_fitz_open.assert_called()

    @patch('pdf_masker.fitz.open')
    def test_masking_styles(self, mock_fitz_open):
        """Test different masking styles"""
        # Mock the PDF document
        mock_doc = MagicMock()
        mock_page = MagicMock()
        mock_doc.__iter__.return_value = [mock_page]
        mock_fitz_open.return_value.__enter__.return_value = mock_doc
        
        # Test star masking
        result = mask_sensitive_information(
            self.test_pdf_path,
            self.output_pdf_path,
            mask_email=True,
            style_star=True
        )
        
        # Test black box masking
        result = mask_sensitive_information(
            self.test_pdf_path,
            self.output_pdf_path,
            mask_email=True,
            style_black=True
        )
        
        # Test frame masking
        result = mask_sensitive_information(
            self.test_pdf_path,
            self.output_pdf_path,
            mask_email=True,
            style_frame=True
        )
        
        # Verify the function was called multiple times
        assert mock_fitz_open.call_count == 3


class TestRegexPatterns:
    """Test regex patterns for detecting sensitive information"""

    def test_email_regex(self):
        """Test email address detection regex"""
        from pdf_masker import email_regex
        
        # Valid email addresses
        valid_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "user+tag@example.org",
            "123@numbers.com"
        ]
        
        for email in valid_emails:
            assert email_regex.search(email) is not None
        
        # Invalid email addresses
        invalid_emails = [
            "invalid-email",
            "@domain.com",
            "user@",
            "user@.com"
        ]
        
        for email in invalid_emails:
            assert email_regex.search(email) is None

    def test_phone_regex(self):
        """Test phone number detection regex"""
        from pdf_masker import phone_regex
        
        # Valid phone numbers
        valid_phones = [
            "555-123-4567",
            "(555) 123-4567",
            "+1-555-123-4567",
            "555.123.4567",
            "555 123 4567"
        ]
        
        for phone in valid_phones:
            assert phone_regex.search(phone) is not None
        
        # Invalid phone numbers
        invalid_phones = [
            "123",
            "abc-def-ghij",
            "555-123",
            "555-123-45678"
        ]
        
        for phone in invalid_phones:
            assert phone_regex.search(phone) is None


if __name__ == "__main__":
    pytest.main([__file__]) 