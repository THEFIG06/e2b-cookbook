import openai

from typing import List
from openai.types.beta.assistant_create_params import Tool


client = openai.Client()

functions: List[Tool] = [
    {
        "type": "function",
        "function": {
            "name": "saveCodeToFile",
            "description": "Save code to file",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "The code to save",
                    },
                    "filename": {
                        "type": "string",
                        "description": "The filename including the path and extension",
                    },
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "listFiles",
            "description": "List files in a directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "The path to the directory",
                    },
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "readFile",
            "description": "Read a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "The path to the file",
                    },
                },
            },
        },
    },
]

ai_developer = client.beta.assistants.create(
    instructions="""You are an AI developer.
When given a coding task, write and save code to files and install any packages if needed.
Start by listing all files inside the repo. You work inside the '/home/user/repo' directory.
Don't argue with me and just complete the task.
""",
    name="AI Developer",
    tools=functions,
    model="gpt-4-1106-preview",
)