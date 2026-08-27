from pathlib import Path
from datetime import datetime

root_folder = Path("files")

for path in root_folder.glob("**/*"):
    if path.is_file():
        stats = path.stat()
        second_created = stats.st_birthtime  # Get the creation time of the file in seconds since the epoch
        date_created = datetime.fromtimestamp(second_created).strftime("%Y-%m-%d")  # Convert the creation time to a formatted date string
                    
        new_filename = f"{path.stem}_{date_created}{path.suffix}"  # Create a new filename based on the parent folder name
        print(path,end=" ")  # Print the path of each file and directory in the root folder
        print("should be renamed to ", end="")  # Print a message indicating the new filename
        print(path.parent / new_filename)  # Print the new filename
        # uncomment the following line to actually rename the files
        # path.rename(path.parent / new_filename)  # Rename the file with the new filename