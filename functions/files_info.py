import os

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir

    if directory:
        target_dir = os.path.abspath(os.path.join(abs_working_dir, directory))
    
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_string_repr = []
        for file_name in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file_name)
            file_size = 0
            file_size = os.path.getsize(file_path)
            if os.path.isdir(file_path):
                dir_string_repr.append(f"- {file_name}: file_size={file_size}, is_dir=True")
            else:
                dir_string_repr.append(f"- {file_name}: file_size={file_size}, is_dir=False")
        
        return "\n".join(dir_string_repr)
    except Exception as e:
        return f"Error listing files: {e}"
    

            
    
    
    
    