import sys
from frontend_app.gradio_interface import display_schema, upload_pdf

if __name__ == "__main__":
    # Ensure the correct Python path is set for module imports
    sys.path.insert(0, '.')

    import gradio as gr

    # Gradio Interface
    with gr.Blocks() as ui:
        with gr.Tab("Schema Viewer"):
            output = gr.Markdown(label="Schema Details", value=display_schema())

        file_input = gr.File(label="Upload PDF")
        output = gr.JSON(label="Extracted Data")
        missing_output = gr.JSON(label="Missing Data")

        file_input.upload(upload_pdf, inputs=file_input, outputs=[output, missing_output])

    ui.launch()