import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text to a file, contstrained to working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path, relative to the current working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the contents that will be written to the file",
            )
        },
    ),
)

# Writes text content to a file, creates the file if it doesn't exist
def write_file(working_directory, file_path, content):
    abs_working = os.path.abspath(working_directory)
    file_location = abs_working + '/' +file_path 
    if not os.path.abspath(file_location).startswith(abs_working):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    # Check if file exists if not create it
    try:
        with open(file_location, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'