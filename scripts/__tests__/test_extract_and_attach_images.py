import os
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock

# Add scripts directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import extract_and_attach_images

class TestExtractAndAttachImages(unittest.TestCase):
    def test_extract_images_from_invalid_docx(self):
        with tempfile.NamedTemporaryFile(suffix='.docx') as tmp:
            tmp.write(b"not a valid zip docx")
            tmp.flush()
            result = extract_and_attach_images.extract_images_from_docx(tmp.name)
            self.assertEqual(result, [])

    @patch("extract_and_attach_images.get_paper_mappings")
    @patch("extract_and_attach_images.find_source_docx_files")
    def test_process_all_papers_no_files(self, mock_find_docx, mock_get_manifest):
        mock_get_manifest.return_value = []
        mock_find_docx.return_value = []
        
        # Should execute without errors
        extract_and_attach_images.process_all_papers()
        mock_get_manifest.assert_called_once()
        mock_find_docx.assert_called_once()

if __name__ == '__main__':
    unittest.main()
