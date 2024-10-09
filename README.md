
# AI Schema Filler

This project uses OpenAI's GPT-4 to extract structured data from documents and map them to a predefined schema. It employs Python, Flask, and OpenAI's API for text processing. The environment configuration is managed using `.env` files.

## Features

- Extracts structured data from PDF or text documents.
- Maps extracted data to a predefined schema.
- Handles JSON formatting for compatibility with data validation.
- Uses `dotenv` for secure handling of API keys.
- Gradio or Streamlit frontend to upload documents for processing.

## Project Structure

```bash
.
├── backend/
│   ├── app.py                 # Flask app entry point
│   ├── services/
│   │   ├── pdf_parser.py      # Service to extract text from PDFs
│   │   ├── gpt4_service.py    # Service to call GPT-4 for data extraction
│   │   ├── schema_mapping.py  # Service to map extracted data to schema
│   │   ├── validation_service.py # Service to validate the data against the schema
├── frontend/
│   ├── interface.py           # Gradio or Streamlit interface for uploading files
├── .env                       # Environment variables (not checked into version control)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
```

## Requirements

1. **Python 3.9+**
2. **Virtual Environment (optional but recommended)**

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-schema-filler.git
cd ai-schema-filler
```

### Step 2: Set up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
# or
venv\Scripts\Activate  # For Windows
```

### Step 3: Install the Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up Environment Variables

Create a `.env` file in the root of the project:

```bash
touch .env
```

Add your OpenAI API key and other environment variables in `.env`:

```sh
OPENAI_API_KEY=your-openai-api-key
```

### Step 5: Run the Backend Server

```bash
cd backend
python app.py
```

### Step 6: Run the Frontend Interface

In a separate terminal:

```bash
cd frontend
python interface.py
```

## Usage

1. **Frontend**: You can use the frontend (Gradio/Streamlit) to upload a PDF or text file. The file will be processed, and the data will be extracted, mapped to the schema, and returned in JSON format.

2. **Backend**: The Flask backend exposes an API endpoint (`/process_pdf`) to receive files, extract text from them, and map the data to the predefined schema.

### API Example

**POST** `/process_pdf`

**Request:**
- `file`: PDF file to be processed.

**Response:**
```json
{
  "mapped_data": {
    // extracted data mapped to schema
  },
  "missing_data": {
    "required": [],
    "desired": []
  }
}
```

## Example Schema

The schema used to map extracted data:

```json
{
  "project": "curriculum_company_name",
  "sections": {
    "summary_of_qualifications": {
      "professional_background": {
        "item": "string",
        "required": true
      },
      "experience": {
        "item": "string",
        "required": true
      },
      "applications": {
        "item": "array",
        "minItems": 1,
        "schema": { "item": "string" }
      }
    },
    "skills": {
      "item": "array",
      "minItems": 1,
      "schema": {
        "item": "object",
        "properties": {
          "name": { "item": "string", "required": true },
          "level": { "item": "string" }
        }
      }
    }
    // other sections...
  }
}
```

## Environment Variables
```sh
- OPENAI_API_KEY: Your OpenAI API key, stored in the .env file.
```

## Troubleshooting

- Ensure that your `.env` file is set up correctly and contains your OpenAI API key.
- Check the `requirements.txt` file to ensure all dependencies are installed.
- If encountering JSON errors, verify that the response from the GPT-4 model is in the correct format.

## Contribution

Feel free to fork the repository, create pull requests, or raise issues if you encounter bugs or have suggestions for improvements.

## License

MIT License
