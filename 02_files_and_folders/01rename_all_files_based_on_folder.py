from pathlib import Path

root_folder = Path("files")
root_folder2 = Path("files2")

# print all filenames one subdirectory away from the root folder
file_paths1 = root_folder.iterdir()  # Get an iterator of all files and directories in the root folder
for path in file_paths1:
    if path.is_dir():
        for filepath in path.iterdir():
            print(filepath)  # Print the path of each file in the subdirectory

print("\n\n")  # Print newlines for better readability

# print all filenames in the root folder and all subdirectories recursively
file_paths2 = root_folder.glob("**/*")  # Get an iterator of all files and directories in the root folder
for path in file_paths2:
    if path.is_file():
        new_filename = f"{path.parent.name}_{path.name}"  # Create a new filename based on the parent folder name
        print(path,end=" ")  # Print the path of each file and directory in the root folder
        print("should be renamed to ", end="")  # Print a message indicating the new filename
        print(path.parent / new_filename)  # Print the new filename
        # uncomment the following line to actually rename the files
        # path.rename(path.parent / new_filename)  # Rename the file with the new filename

print("\n\n")  # Print newlines for better readability

# print all filenames in the root folder and all subdirectories recursively
file_paths3 = root_folder2.glob("**/*")  # Get an iterator of all files and directories in the root folder
for path in file_paths3:
    if path.is_file():
        parent_folder = path.parts
        subfolders = path.parts[1:-1]  # Get all the subfolders in the path
        combine_subfolders = "_".join(subfolders)  # Combine the subfolder names with underscores

        new_filename = f"{combine_subfolders}_{path.name}"  # Create a new filename based on the combined subfolder names
        print(path,end=" ")  # Print the path of each file and directory in the root folder
        print("should be renamed to ", end="")  # Print a message indicating the new filename
        print(path.parent / new_filename)  # Print the new filename
        # uncomment the following line to actually rename the files
        # path.rename(path.parent / new_filename)  # Rename the file with the new filename