import os
from google.genai import types

MAX_CHARS = 10000

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a file in a file path, \
                upto a limit if maximum characters, \
                constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file \
                    to get content from, \
                    relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_dir, file_path):
    abs_working_directory = os.path.abspath(working_dir)
    target_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    if not target_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(target_path, "r") as f:
        file_content_string = f.read()
        if len(file_content_string) > MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS+1] + f'[...File "{file_path}" truncated at 10000 characters]'       
    
    return file_content_string
    
    

