import gradio as gr
import requests

def upload_pdf(file):
    # Open the file using 'rb' mode to send in the correct binary format
    with open(file.name, 'rb') as f:
        files = {'file': (file.name, f, 'application/pdf')}
        response = requests.post("http://localhost:5000/process_pdf", files=files)
        result = response.json()

    return result['mapped_data'], result['missing_data']

# Gradio Interface
with gr.Blocks() as ui:
    file_input = gr.File(label="Upload PDF")
    output = gr.JSON(label="Extracted Data")
    missing_output = gr.JSON(label="Missing Data")

    file_input.upload(upload_pdf, inputs=file_input, outputs=[output, missing_output])

ui.launch()