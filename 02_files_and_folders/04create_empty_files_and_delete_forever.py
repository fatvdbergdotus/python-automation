from pathlib import Path

root_folder = Path("empty_files")

# Create empty files in the specified folder
for i in range(20):
    new_file = root_folder / f"file_{i}.txt"  # Create a new file path with a unique name
    new_file.touch()  # Create an empty file at the specified path
    print(f"Created empty file: {new_file}")  # Print a message indicating the creation of the file

# Delete the content of the created files forever
for path in root_folder.glob("*.txt"):
    if path.is_file():
        with open(path, "wb") as file:
            file.write(b'')  # Write an empty byte string to the file, effectively deleting its content
        path.unlink()  # Delete the file from the filesystem

# Create empty files in the specified folder (again)
for i in range(20):
    new_file = root_folder / f"file_{i}.txt"  # Create a new file path with a unique name
    new_file.touch()  # Create an empty file at the specified path
    print(f"Created empty file: {new_file}")  # Print a message indicating the creation of the file