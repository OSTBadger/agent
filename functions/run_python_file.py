
import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional arguments supplied to the python program",
            )
        },
    ),
)

#Runs a python file
def run_python_file(working_directory, file_path, args=[]):
    abs_working = os.path.abspath(working_directory)
    file_location = abs_working + '/' +file_path 
    if not os.path.abspath(file_location).startswith(abs_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_location):
        print(file_path)
        return f'Error: File "{file_path}" not found.'
    if not file_location.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    # Run python file, timeout 30s,capture stdout and stderr,set working dir, pass args
    
    cmd_list =["python",file_location]
    if args:
        for ar in args:
            cmd_list.append(ar)
    try:
        result = subprocess.run(cmd_list,cwd=abs_working,timeout=30,capture_output=True,text=True)
        output = f'STDOUT:\n{result.stdout}\nSTDERR\n{result.stderr}'
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}'
    except Exception as e:
        return f"Error: executing Python file: {e}"
    return output