from flask import Flask, request, jsonify
from services import pdf_parser, gpt4_service, schema_mapping, validation_service
import os
import json

app = Flask(__name__)

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    # Extract file from request
    pdf_file = request.files.get('file')
    if not pdf_file:
        return jsonify({"error": "No file uploaded"}), 400

    # Save the file temporarily
    temp_file_path = os.path.join('/tmp', pdf_file.filename)
    pdf_file.save(temp_file_path)

    # Extract text from the saved file
    text = pdf_parser.extract_text(temp_file_path)

    # open extracted text file if exists do not use gpt4, just use the extracted text
    if os.path.exists('/Users/s.vega/dev/personal/translate-document-format/ai-schema-filler/extracted_data.txt'):
        with open('/Users/s.vega/dev/personal/translate-document-format/ai-schema-filler/extracted_data.txt', 'r') as f:
            extracted_data = json.load(f)
    else:
        # Pass text to GPT-4 for extraction
        extracted_data = gpt4_service.extract_data(text)

        # save the extracted data to a file named extracted_data.txt
        with open('/Users/s.vega/dev/personal/translate-document-format/ai-schema-filler/extracted_data.txt', 'w') as f:
            json.dump(extracted_data, f)

    # Map to schema
    mapped_data = schema_mapping.map_to_schema(extracted_data)
    # Validate against the schema
    missing_data = validation_service.validate(mapped_data)
    return jsonify({
        'mapped_data': mapped_data,
        'missing_data': missing_data
    })

if __name__ == '__main__':
    app.run(debug=True)