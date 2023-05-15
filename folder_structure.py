import os

def create_folder_tree(root_directory, output_file):
    with open(output_file, 'w') as file:
        write_folder_tree(root_directory, file)

def write_folder_tree(directory, file, indent=''):
    file.write(f"{indent}[{os.path.basename(directory)}]\n")
    indent += '    '
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) and item != 'venv':  # Skip 'venv' folder
            write_folder_tree(item_path, file, indent)
        elif os.path.isfile(item_path):
            file.write(f"{indent}{item}\n")

root_directory = os.getcwd()  # Use the current working directory as the root directory
output_file = 'structure.txt'
create_folder_tree(root_directory, output_file)
print(f"Folder structure saved in {output_file} successfully!")



