from pathlib import Path

new_extension = ".csv"  # Specify the new file extension

root_folder = Path("files")

for path in root_folder.glob("**/*"):
    if path.is_file():
        new_filename = path.with_suffix(new_extension)  # Create a new filename with the new extension

        print(path,end=" ")  # Print the path of each file and directory in the root folder
        print("should be renamed to ", end="")  # Print a message indicating the new filename
        print(path.parent / new_filename)  # Print the new filename