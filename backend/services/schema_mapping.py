from models.schema import SCHEMA

def map_to_schema(extracted_data):
    mapped_data = {}

    # Logic to match extracted data to the predefined schema
    for section, details in SCHEMA['sections'].items():
        mapped_data[section] = extracted_data.get(section, None)

    return mapped_data