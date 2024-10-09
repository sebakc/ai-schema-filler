import gradio as gr
from backend.models.schema import SCHEMA
import json
import requests

def upload_pdf(file):
    # Open the file using 'rb' mode to send in the correct binary format
    with open(file.name, 'rb') as f:
        files = {'file': (file.name, f, 'application/pdf')}
        response = requests.post("http://localhost:5000/process_pdf", files=files)
        result = response.json()

    return result['mapped_data'], result['missing_data']


def display_schema():
    # Build a list of sections and their fields with details
    schema_data = []
    
    for section_name, section_details in SCHEMA['sections'].items():
        schema_data.append(f"### Section: {section_name}")
        schema_data.append(f"- Description: {section_details.get('description', 'No description available')}")
        schema_data.append(f"- Type: {section_details.get('item', 'Not specified')}")

        # Loop through the properties (fields)
        if 'properties' in section_details:
            for field_name, field_details in section_details['properties'].items():
                schema_data.append(f"  - **Field: {field_name}**")
                schema_data.append(f"    - Description: {field_details.get('description', 'No description available')}")
                schema_data.append(f"    - Type: {field_details.get('item', 'Not specified')}")
                schema_data.append(f"    - Required: {field_details.get('required', False)}")
                schema_data.append(f"    - Desired: {field_details.get('desired', False)}")

    return "\n".join(schema_data)

def convert_to_html(data, indent=0):
    """Converts a dictionary or list into an HTML structure."""
    html = ""
    if isinstance(data, dict):
        for key, value in data.items():
            html += f"<div style='margin-left: {indent * 20}px'><strong>{key}:</strong>"
            html += convert_to_html(value, indent + 1)
            html += "</div>"
    elif isinstance(data, list):
        for item in data:
            html += f"<div style='margin-left: {indent * 20}px'>- {convert_to_html(item, indent + 1)}</div>"
    else:
        html += f" {data}"
    return html

def generate_questions(missing_data):
    """Generate questions based on the missing data."""
    questions = []
    for field in missing_data.get('required', []):
        section, question_key = field.split(".")
        section_data = SCHEMA['sections'].get(section, {})
        field_data = section_data.get('properties', {}).get(question_key, {})
        question_text = field_data.get('question', f"Please provide {question_key}")
        questions.append(question_text)
    return questions


# Gradio Interface
with gr.Blocks() as ui:
    with gr.Tab("Schema Viewer"):
        schema_output = gr.Markdown(value=display_schema())

    with gr.Tab("Upload PDF"):
        file_input = gr.File(label="Upload PDF")
        output_json = gr.JSON(label="Extracted Data")
        output_html = gr.HTML(label="Extracted Data (Readable Format)")
        
        missing_output = gr.JSON(label="Missing Data")
        questions_output = gr.JSON(label="Generated Questions")

        # When PDF is uploaded, update the outputs
        def handle_upload(file):
            mapped_data, missing_data = upload_pdf(file)
            readable_html = convert_to_html(mapped_data)  # Convert data to HTML format
            
            # Generate questions for the missing fields (as an array of values)
            questions = generate_questions(missing_data)
            
            return mapped_data, readable_html, missing_data, questions

        file_input.upload(handle_upload, inputs=file_input, outputs=[output_json, output_html, missing_output, questions_output])

ui.launch(debug=True)