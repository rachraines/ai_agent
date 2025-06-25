import os

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
        output_lines = []
        for item in os.listdir(target_directory):
            item_path = os.path.join(target_directory, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            output_lines.append (f'- {item}: file_size={size} bytes, is_dir={is_dir}')

        return '\n'.join(output_lines)
    
    except Exception as e:
        return(f'Error listing files: {e}')

def get_file_content(working_directory, file_path):
    # Maps the path to the working directory, and assigns it to file_path
    abs_working_directory = os.path.abspath(working_directory)
    target_file_path = abs_working_directory

    # Joins the path of file_path (if it exists) to the working directory
    if file_path:
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
    # Checks if file_path is inside the working directory
    if not target_file_path.startswith(abs_working_directory):
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        
    # Checks if the file exists and is a file
    if not os.path.isfile(target_file_path):
        return(f'Error: File not found or is not a regular file: "{file_path}"')

    try:
        # Reads and returns contents of file up to 10000 chars
        max_chars = 10000
        with open(target_file_path, "r") as f:
            content = f.read()

        # Truncates the file if more than 10000 chars    
        if len(content) > 10000:
                return content[:10000] + f'[...File "{file_path}" truncated at 10000 characters]'
        return content
    
    except Exception as e:
        return(f'Error reading file: {e}')
    
def write_file(working_directory, file_path, content):
    # Maps the path to the working directory, and assigns it to file_path
    abs_working_directory = os.path.abspath(working_directory)
    target_file_path = abs_working_directory

    # Joins the path of file_path (if it exists) to the working directory
    if file_path:
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
    # Checks if file_path is inside the working directory
    if not target_file_path.startswith(abs_working_directory):
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        
    try:
        # Writes the file (creates if not exists, overwrites if it does)
        with open(target_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{target_file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return(f'Error creating file: {e}')
