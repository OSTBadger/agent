import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

# Retuns the file names and sizes in a directory
def get_files_info(working_directory, directory="."):
    abs_working = os.path.abspath(working_directory)
    joined_directory = os.path.join(abs_working, directory)
    
    if not (os.path.abspath(joined_directory).startswith(abs_working)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(joined_directory):
        return f'Error: "{directory}" is not a directory'
    contents = os.listdir(joined_directory)
    content_info = ''
    for c in contents:
        name = c
        try:
            size = os.path.getsize(joined_directory+'/'+c)
            directory_bool = os.path.isdir(joined_directory+'/'+c)
            content_info += f'- {name}: file_size={size} bytes, is_dir={directory_bool}\n'
        except Exception as e:
            return f'Error {e}'
    return content_info[:-1]