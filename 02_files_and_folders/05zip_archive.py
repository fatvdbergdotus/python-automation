from pathlib import Path
import zipfile

root_source_folder = Path("empty_files")
root_destination_folder = Path("unzipped_files")
archive_name = root_source_folder / "archive.zip"

# Create a zip archive and add all .txt files from the root folder and its subdirectories
with zipfile.ZipFile(archive_name, 'w') as archive:
    for path in root_source_folder.rglob("*.txt"):
        if path.is_file():
            archive.write(path, arcname=path.relative_to(root_source_folder))  # Add the file to the archive with a relative path
            print(f"Added {path} to {archive_name}")  # Print a message indicating the addition of the file to the archive

# Unzip the archive into the destination folder
with zipfile.ZipFile(archive_name, 'r') as archive:
    archive.extractall(root_destination_folder)  # Extract all files from the archive to the destination folder
    print(f"Extracted {archive_name} to {root_destination_folder}")  # Print a message indicating the extraction of the archive
