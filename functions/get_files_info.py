import os
import subprocess

def get_files_info(working_directory, directory=None):
    # Maps the path to the working directory, and assigns it to directory
    abs_working_directory = os.path.abspath(working_directory)
    target_directory = abs_working_directory

    # Joins the path of directory (if it exists) to the working directory
    if directory:
        target_directory = os.path.abspath(os.path.join(working_directory,directory))
        
    # Checks if directory is inside the working directory
    if not target_directory.startswith(abs_working_directory):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        
    # Checks if the directory exists and is a directory
    if not os.path.isdir(target_directory):
        return(f'Error: "{directory}" is not a directory')
        
    try:     
        # Reads and returns the contents of the directory
        files_info = []
        for filename in os.listdir(target_directory):
            filepath = os.path.join(target_directory, filename)
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            files_info.append(
                f'- {filename}: file_size={file_size} bytes, is_dir={is_dir}')

        return '\n'.join(files_info)
    
    except Exception as e:
        return(f'Error listing files: {e}')

def get_file_content(working_directory, file_path):
    # Maps the path to the working directory, and assigns it to file_path
    abs_working_directory = os.path.abspath(working_directory)
     # Joins the path of file_path (if it exists) to the working directory
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    # Checks if file_path is inside the working directory
    if not abs_file_path.startswith(abs_working_directory):
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        
    # Checks if the file exists and is a file
    if not os.path.isfile(abs_file_path):
        return(f'Error: File not found or is not a regular file: "{file_path}"')

    try:
        # Reads and returns contents of file up to 10000 chars
        max_chars = 10000
        with open(abs_file_path, "r") as f:
            content = f.read(max_chars)

            # Truncates the file if more than 10000 chars    
            if os.path.getsize(abs_file_path) > max_chars:
                content += (
                    f'[...File "{file_path}" truncated at {max_chars} characters]'
                )
        return content
    
    except Exception as e:
        return(f'Error reading file: {e}')
    
def write_file(working_directory, file_path, content):
    # Maps the path to the working directory, and assigns it to file_path
    abs_working_directory = os.path.abspath(working_directory)
    # Joins the path of file_path (if it exists) to the working directory
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
    # Checks if file_path is inside the working directory
    if not abs_file_path.startswith(abs_working_directory):
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.exists(abs_file_path):  
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"
    
def run_python_file(working_directory, file_path, args=None):
    # Maps the path to the working directory, and assigns it to file_path
    abs_working_directory = os.path.abspath(working_directory)
        # Joins the path of file_path (if it exists) to the working directory
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
    # Checks if file_path is inside the working directory
    if not abs_file_path.startswith(abs_working_directory):
        return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    # Checks if the file exists
    if not os.path.exists(abs_file_path):
        return(f'Error: File "{file_path}" not found.')
    
    # Checks if the file ends with ".py"
    if not file_path.endswith(".py"):
        return(f'Error: "{file_path}" is not a Python file.')
        
    # Execute the Python file
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            timeout=30,
            cwd=abs_working_directory,
            text=True
        )

        output = []
        if result.stdout:
            output.append(f'STDOUT:\n{result.stdout}')
        if result.stderr:
            output.append(f'STDERR:{result.stderr}')
        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')
        if not output:
            return "No output produced."
        
        return "\n".join(output)
    
    except Exception as e:
        return f'Error: executing Python file: {e}'