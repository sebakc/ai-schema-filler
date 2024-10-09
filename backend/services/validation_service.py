from models.schema import SCHEMA

def validate(mapped_data):
    missing = {'required': [], 'desired': []}

    # Check for required and desired fields in each section
    for section, details in SCHEMA['sections'].items():
        if section not in mapped_data:
            # If the entire section is missing, add all required fields from this section
            if 'properties' in details:
                for field, config in details['properties'].items():
                    if config.get('required', False):
                        missing['required'].append(f"{section}.{field}")
                    elif config.get('desired', False):
                        missing['desired'].append(f"{section}.{field}")
            elif details['item'] == 'array' and 'minItems' in details:
                # Handle array-type sections without 'properties'
                missing['required'].append(f"{section} (minItems not met)")
        else:
            # If the section exists, check individual fields within the section
            if 'properties' in details:
                for field, config in details['properties'].items():
                    if field not in mapped_data[section]:
                        if config.get('required', False):
                            missing['required'].append(f"{section}.{field}")
                        elif config.get('desired', False):
                            missing['desired'].append(f"{section}.{field}")
                    else:
                        # If the field is an array, check if it meets the 'minItems' condition
                        if config['item'] == 'array' and 'minItems' in config:
                            if len(mapped_data[section][field]) < config['minItems']:
                                missing['required'].append(f"{section}.{field} (minItems not met)")
            else:
                # If the section doesn't have 'properties', handle it as an array or object
                if details['item'] == 'array' and 'minItems' in details:
                    if len(mapped_data[section]) < details['minItems']:
                        missing['required'].append(f"{section} (minItems not met)")
    
    return missing