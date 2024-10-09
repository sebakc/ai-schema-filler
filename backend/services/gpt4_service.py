from openai import OpenAI
from models.schema import SCHEMA
import json
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key from the environment variable
client = OpenAI(api_key=api_key)



def extract_data(text):
    # Formulating the prompt
    prompt = f"Extract the following data from this document: {text}."
    
    # Create a schema prompt for the structure
    schema_prompt = f"""
    The response must be in valid JSON format with the following structure:
    {SCHEMA['sections']}.
    Do not include any explanations, comments, or formatting like triple backticks. 
    Just return the JSON object directly. Make sure all fields match the schema and values are properly formatted.
    """
    # Call GPT-4 with the formatted prompts
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": schema_prompt},
            {"role": "user", "content": prompt}
        ])

    # Extract the content from the response
    response_text = response.choices[0].message.content

    try:
        # Directly load the response into a JSON object
        extracted_data = json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

    return extracted_data