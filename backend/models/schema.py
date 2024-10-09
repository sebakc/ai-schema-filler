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
                    "required": True,
                    "question": "Can you describe your professional background briefly?"
                },
                "experience": {
                    "item": "string",
                    "description": "Total years/months of experience",
                    "required": True,
                    "question": "How many total years/months of experience do you have?"
                },
                "applications": {
                    "item": "array",
                    "description": "Types of applications the candidate has worked on",
                    "minItems": 1,
                    "schema": {
                        "item": "string",
                        "description": "A type of application"
                    },
                    "question": "What types of applications have you worked on?"
                },
                "technologies": {
                    "item": "array",
                    "description": "List of main technologies the candidate has experience with",
                    "minItems": 1,
                    "schema": {
                        "item": "string",
                        "description": "A technology"
                    },
                    "question": "What are the main technologies you have experience with?"
                },
                "methodologies": {
                    "item": "array",
                    "description": "Software development methodologies used",
                    "minItems": 1,
                    "schema": {
                        "item": "string",
                        "description": "A methodology"
                    },
                    "question": "What software development methodologies have you used?"
                },
                "sd_life_cycle": {
                    "item": "array",
                    "description": "Stages of the software development life cycle the candidate is familiar with",
                    "minItems": 1,
                    "schema": {
                        "item": "string",
                        "description": "A stage in the software development life cycle"
                    },
                    "question": "Which stages of the software development life cycle are you familiar with?"
                },
                "architecture_attributes": {
                    "item": "array",
                    "description": "Attributes of the architecture worked on",
                    "schema": {
                        "item": "string",
                        "description": "An architecture attribute"
                    },
                    "question": "What are the attributes of the architecture you have worked on?"
                },
                "interests": {
                    "item": "array",
                    "description": "Interests in IT",
                    "schema": {
                        "item": "string",
                        "description": "An interest in IT"
                    },
                    "question": "What are your interests in IT?"
                },
                "personal_qualities": {
                    "item": "array",
                    "description": "Personal qualities of the candidate",
                    "schema": {
                        "item": "string",
                        "description": "A personal quality"
                    },
                    "question": "What personal qualities do you possess that are relevant to your work?"
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
                        "required": True,
                        "question": "What are the names of the skills you possess?"
                    },
                    "level": {
                        "item": "string",
                        "description": "The proficiency level of the skill (optional)",
                        "question": "What is the proficiency level of this skill?"
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
                        "required": True,
                        "question": "What is the name of the project?"
                    },
                    "description": {
                        "item": "string",
                        "description": "Description of the project",
                        "required": True,
                        "question": "What is the project about?"
                    },
                    "customer": {
                        "item": "string",
                        "description": "Customer for whom the project was done",
                        "required": False,
                        "question": "Who was the customer for this project?"
                    },
                    "duration": {
                        "item": "string",
                        "description": "Duration of the project",
                        "required": True,
                        "question": "What was the duration of this project?"
                    },
                    "role": {
                        "item": "string",
                        "description": "Role in the project",
                        "required": True,
                        "question": "What was your role in this project?"
                    },
                    "responsibilities": {
                        "item": "array",
                        "description": "Responsibilities during the project",
                        "minItems": 1,
                        "schema": {
                            "item": "string",
                            "description": "A responsibility"
                        },
                        "question": "What were your responsibilities during this project?"
                    },
                    "team_size": {
                        "item": "string",
                        "description": "Size of the team",
                        "required": False,
                        "question": "How large was the team?"
                    },
                    "tools_technologies": {
                        "item": "array",
                        "description": "Tools and technologies used in the project",
                        "schema": {
                            "item": "string",
                            "description": "A tool or technology"
                        },
                        "question": "What tools and technologies were used in the project?"
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
                        "required": True,
                        "question": "What is the name of the certification?"
                    },
                    "year": {
                        "item": "string",
                        "description": "The year the certification was obtained",
                        "required": False,
                        "question": "When was this certification obtained?"
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
                    "required": True,
                    "question": "What degree did you obtain?"
                },
                "school_name": {
                    "item": "string",
                    "description": "Name of the school/university",
                    "required": True,
                    "question": "What is the name of the school/university?"
                },
                "department": {
                    "item": "string",
                    "description": "Department/Field of study",
                    "required": False,
                    "question": "What was your field of study or department?"
                }
            }
        }
    }
}