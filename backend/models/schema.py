SCHEMA = {
    "project": "curriculum_company_name",
    "description": "This is the format of company_name. The user should fill this format, and they must fit their CV within this structure.",
    "sections": {
        "summary_of_qualifications": {
            "item": "object",
            "name": "summary_of_qualifications",
            "description": "A summary of the candidate's qualifications",
            "properties": {
                "professional_background": {
                    "item": "string",
                    "description": "Please provide a brief description of your professional background",
                    "required": True
                },
                "experience": {
                    "item": "string",
                    "description": "Total years/months of experience",
                    "required": True
                },
                "applications": {
                    "item": "array",
                    "description": "Types of applications the candidate has worked on",
                    "minItems": 1,
                    "schema": {
                        "item": "string",
                        "description": "A type of application"
                    }
                },
                "technologies": {
                    "item": "array",
                    "description": "List of main technologies the candidate has experience with",
                    "minItems": 1,
                    "schema": {
                        "item": "string",
                        "description": "A technology"
                    }
                },
                "methodologies": {
                    "item": "array",
                    "description": "Software development methodologies used",
                    "minItems": 1,
                    "schema": {
                        "item": "string",
                        "description": "A methodology"
                    }
                },
                "sd_life_cycle": {
                    "item": "array",
                    "description": "Stages of the software development life cycle the candidate is familiar with",
                    "minItems": 1,
                    "schema": {
                        "item": "string",
                        "description": "A stage in the software development life cycle"
                    }
                },
                "architecture_attributes": {
                    "item": "array",
                    "description": "Attributes of the architecture worked on",
                    "schema": {
                        "item": "string",
                        "description": "An architecture attribute"
                    }
                },
                "interests": {
                    "item": "array",
                    "description": "Interests in IT",
                    "schema": {
                        "item": "string",
                        "description": "An interest in IT"
                    }
                },
                "personal_qualities": {
                    "item": "array",
                    "description": "Personal qualities of the candidate",
                    "schema": {
                        "item": "string",
                        "description": "A personal quality"
                    }
                }
            }
        },
        "skills": {
            "item": "array",
            "name": "skills",
            "description": "A list of skills",
            "minItems": 1,
            "schema": {
                "item": "object",
                "description": "A skill with a name and an optional level",
                "properties": {
                    "name": {
                        "item": "string",
                        "description": "The name of the skill",
                        "required": True
                    },
                    "level": {
                        "item": "string",
                        "description": "The proficiency level of the skill (optional)"
                    }
                }
            }
        },
        "experience": {
            "item": "array",
            "name": "experience",
            "description": "A list of professional experiences",
            "minItems": 1,
            "schema": {
                "item": "object",
                "description": "Details of a professional experience",
                "properties": {
                    "project_name": {
                        "item": "string",
                        "description": "Name of the project",
                        "required": True
                    },
                    "description": {
                        "item": "string",
                        "description": "Description of the project",
                        "required": True
                    },
                    "customer": {
                        "item": "string",
                        "description": "Customer for whom the project was done",
                        "required": False
                    },
                    "duration": {
                        "item": "string",
                        "description": "Duration of the project",
                        "required": True
                    },
                    "role": {
                        "item": "string",
                        "description": "Role in the project",
                        "required": True
                    },
                    "responsibilities": {
                        "item": "array",
                        "description": "Responsibilities during the project",
                        "minItems": 1,
                        "schema": {
                            "item": "string",
                            "description": "A responsibility"
                        }
                    },
                    "team_size": {
                        "item": "string",
                        "description": "Size of the team",
                        "required": False
                    },
                    "tools_technologies": {
                        "item": "array",
                        "description": "Tools and technologies used in the project",
                        "schema": {
                            "item": "string",
                            "description": "A tool or technology"
                        }
                    }
                }
            }
        },
        "certifications": {
            "item": "array",
            "name": "certifications",
            "description": "A list of certifications",
            "schema": {
                "item": "object",
                "description": "A certification with a name and year",
                "properties": {
                    "name": {
                        "item": "string",
                        "description": "The name of the certification",
                        "required": True
                    },
                    "year": {
                        "item": "string",
                        "description": "The year the certification was obtained",
                        "required": False
                    }
                }
            }
        },
        "education": {
            "item": "object",
            "name": "education",
            "description": "Please provide your education details",
            "properties": {
                "degree": {
                    "item": "string",
                    "description": "Degree obtained",
                    "required": True
                },
                "school_name": {
                    "item": "string",
                    "description": "Name of the school/university",
                    "required": True
                },
                "department": {
                    "item": "string",
                    "description": "Department/Field of study",
                    "required": False
                }
            }
        }
    }
}