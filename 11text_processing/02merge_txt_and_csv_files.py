from pathlib import Path

files_dir = Path("files")

# merge all .txt and .csv files within the files directory into a single file
# the merged content will be stored in the merged_content variable
merged_content = ""
for file_path in files_dir.iterdir():
    if file_path.is_file() and (file_path.suffix == ".txt" or file_path.suffix == ".csv"):
        with open(file_path, "r") as file:
            merged_content += file.read() + "\n"

# write the merged content to a new file named "merged_file.txt"
with open("merged_file.txt", "w") as merged_file:
    merged_file.write(merged_content)

# merge all .txt and .csv files within the files directory into a single file without including headers
merged_content_no_headers = ""
for file_path in files_dir.iterdir():
    if file_path.is_file() and (file_path.suffix == ".txt" or file_path.suffix == ".csv"):
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                merged_content_no_headers += "".join(lines[1:]) + "\n"

# write the merged content without headers to a new file named "merged_file_no_headers.txt"
with open("merged_file_no_headers.txt", "w") as merged_file_no_headers:
    merged_file_no_headers.write(merged_content_no_headers) 