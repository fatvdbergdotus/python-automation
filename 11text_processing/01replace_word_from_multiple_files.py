from pathlib import Path

files_dir = Path("files")
old_word = "price"
new_word = "prijs"

# replace old_word with new_word in all files within the files directory
for file_path in files_dir.iterdir():
    if file_path.is_file():
        with open(file_path, "r+") as file:
            content = file.read()
            content = content.replace(old_word, new_word)
            file.seek(0)
            file.write(content)
            file.truncate()
            print("contents of", file_path, "after replacement:\n", content)

# replace new_word back with old_word in all files within the files directory
for file_path in files_dir.iterdir():
    if file_path.is_file():
        with open(file_path, "r+") as file:
            content = file.read()
            content = content.replace(new_word, old_word)
            file.seek(0)
            file.write(content)
            file.truncate()
            print("contents of", file_path, "after replacement:\n", content)
