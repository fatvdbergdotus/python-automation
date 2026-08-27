from pathlib import Path

search_term = "14"
search_folder = Path("d:/")

# Search for files in the specified folder and its subdirectories that contain the search term in their names
for file_path in search_folder.rglob(f"*{search_term}*"):
    if file_path.is_file():
        print(f"Found file: {file_path}")  # Print the path of each file that matches the search term

