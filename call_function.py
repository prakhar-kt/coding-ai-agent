from google.genai import types

from functions.files_info import schema_get_files_info
from functions.files_content import schema_get_files_content
from functions.run_file import schema_run_file
from functions.write_file import schema_write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_files_content,
        schema_run_file,
        schema_write_file
    ]
)