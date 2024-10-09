import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

from services.gpt4_service import extract_data

def test_extract_data():
    text = "Sample professional background: 10 years of experience."
    result = extract_data(text)
    assert "10 years of experience" in result