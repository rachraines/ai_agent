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
