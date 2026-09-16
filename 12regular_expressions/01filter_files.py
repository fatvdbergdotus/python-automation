# Filter files based on specific criteria
from pathlib import Path
import re

# Define the directory to search and the file extension to filter
directory = Path("filter_files")

# Get a list of all files in the directory
all_files = [f for f in directory.iterdir() if f.is_file()]

# Print the filtered files
print("All files:")
for file in all_files:
    print(file)

# find files between nov 1 and nov 20
pattern =  re.compile(r"nov[a-zA-Z-]*-(:\d|1\d|20).txt", re.IGNORECASE)
nov_files = [f for f in all_files if (m := pattern.search(f.name)) and 1 <= int(m.group(1)) <= 20]

print("\nFiles between Nov 1 and Nov 20:")

for file in nov_files:
    print(file)