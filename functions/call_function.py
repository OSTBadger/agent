from functions.get_file_contents import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from google.genai import types

# Plumbling for functions
def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args
    working_directory = './calculator'
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    
    match function_name:
        case 'get_file_content':
            function_result = get_file_content(working_directory,function_args["file_path"])
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                        )
                        ],
                        )
        case 'get_files_info':
            if 'directory' in function_args:
                function_result = get_files_info(working_directory,function_args["directory"])
            else:
                function_result = get_files_info(working_directory)
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                        )
                        ],
                        )
        case 'run_python_file':
            if 'args' in function_args:
                function_result = run_python_file(working_directory,function_args['file_path'],function_args['args'])
            else:
                function_result = run_python_file(working_directory,function_args['file_path'])

            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                        )
                        ],
                        )
        case 'write_file':
            function_result = write_file(working_directory,function_args['file_path'],function_args['content'])
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                        )
                        ],
                        )
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                        )
                        ],
                        )
    