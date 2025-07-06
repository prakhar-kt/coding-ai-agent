import os
import subprocess
from google.genai import types

schema_run_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with .py extension \
                located at the given file path \
                constrained by the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file \
                    to run, \
                    relative to the working directory.",
            ),
        },
    ),
)

def run_python_file(working_dir, file_path):
    abs_work_dir = os.path.abspath(working_dir)
    target_file_path = os.path.abspath(os.path.join(abs_work_dir, file_path))

    if not target_file_path.startswith(abs_work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file_path):
        return f'Error: File "{file_path}" not found.'
    if not target_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run([
            "python3", target_file_path
        ],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_work_dir,
            check=False
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT: {result.stdout.strip()}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr.strip()}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            return "No output produced."
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"