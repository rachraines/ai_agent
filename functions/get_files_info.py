from pathlib import Path
import os

def get_files_info(working_directory, directory=None):
    # Maps the paths to the given directories
    if directory is not None:
        working_directory = Path(working_directory).resolve()
        directory = Path(directory).resolve()

    # Checks if the directory exists and is a directory
    if not directory.is_dir():
        return(f'Error: "{directory}" is not a directory')
    
    # Checks if directory is inside the working directory
    if working_directory not in directory.parents and working_directory != directory:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    # Reads and returns the contents of the directory
    output_lines = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        output_lines.append (f'- {item}: file_size={size} bytes, is_dir={is_dir}')

    return '\n'.join(output_lines)