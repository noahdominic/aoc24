import os
import re

def replace_function_names_in_file(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Use regex to match `dayXX_0Y` and replace with `partY`
    updated_content = re.sub(r'day\d{2}_0(\d)', r'part\1', content)
    
    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)

def process_directory(directory):
    # Iterate over all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):  # Process only Python files
                file_path = os.path.join(root, file)
                replace_function_names_in_file(file_path)

# Example usage
directory = '.'  # Replace with the path to your directory
process_directory(directory)

