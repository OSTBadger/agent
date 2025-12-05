import os
def write_file(working_directory, file_path, content):
    abs_working = os.path.abspath(working_directory)
    file_location = abs_working + '/' +file_path 
    print(file_location)
    if not os.path.abspath(file_location).startswith(abs_working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    # Check if file exists if not create it
    try:
        with open(file_location, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'