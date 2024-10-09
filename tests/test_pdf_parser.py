import pytest
from services.pdf_parser import extract_text

def test_extract_text():
    pdf_file = "sample.pdf"
    text = extract_text(pdf_file)
    assert len(text) > 0