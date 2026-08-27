from pathlib import Path

root_folder = Path("empty_files")

for i in range(20):
    new_file = root_folder / f"file_{i}.txt"  # Create a new file path with a unique name
    new_file.touch()  # Create an empty file at the specified path
    print(f"Created empty file: {new_file}")  # Print a message indicating the creation of the file