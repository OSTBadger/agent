import os
from config import CHAR_LIMIT
from google.genai import types

schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the files contents as text of a regular file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path, relative to the working directory.",
            ),
        },
    ),
)

# Returns the contents of a regular file
def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        file_location = abs_working + '/' +file_path 
        if not os.path.abspath(file_location).startswith(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_location):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        contents =  ''
        with open(file_location) as f:
            contents = ''.join(f.readlines())
        if len(contents) > CHAR_LIMIT:
            contents = contents[:CHAR_LIMIT] + f'[...File "{file_path}" truncated at {CHAR_LIMIT} characters]'
        return contents
    except Exception as e:
        return f'Error {e}'