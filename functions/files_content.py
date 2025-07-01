from pathlib import Path

MAX_CHARS = 10000

def get_files_content(working_directory, file_path):
    abs_working_directory = Path(working_directory).resolve()
    target_path = (abs_working_directory / file_path).resolve()
    if not str(target_path).startswith(str(abs_working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not target_path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(target_path, "r") as f:
        file_content_string = f.read()
        if len(file_content_string) > MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS+1] + f'[...File "{file_path}" truncated at 10000 characters]'       
    
    return file_content_string
    
    

