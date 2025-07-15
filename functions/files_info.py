from pathlib import Path

from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, \
                constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, \
                relative to the working directory. \
                If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_dir, directory=None):
    abs_working_dir = Path(working_dir).resolve()
    target_dir = abs_working_dir

    if directory:
        target_dir = (abs_working_dir / directory).resolve()
    
    if not str(target_dir).startswith(str(abs_working_dir)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not target_dir.is_dir():
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_string_repr = []
        for file_path in target_dir.iterdir():
            file_name = file_path.name
            file_size = file_path.stat().st_size
            if file_path.is_dir():
                dir_string_repr.append(f"- {file_name}: file_size={file_size}, is_dir=True")
            else:
                dir_string_repr.append(f"- {file_name}: file_size={file_size}, is_dir=False")
        
        return "\n".join(dir_string_repr)
    except Exception as e:
        return f"Error listing files: {e}"
    

            
    
    
    
    