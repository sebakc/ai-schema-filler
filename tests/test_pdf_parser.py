import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

from services.pdf_parser import extract_text

def test_extract_text():
    pdf_file = "sample.pdf"
    text = extract_text(pdf_file)
    assert len(text) > 0