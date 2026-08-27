from pathlib import Path

# example usage of Path to open a file and read its contents
p1=Path("files/abc.txt")
if p1.exists():
    with open(p1, 'r') as file:
        print(file.read())

# example usage of Path to iterate through all files in a directory
p2=Path("files")
for file in p2.iterdir():
    print(file.name)  # print the name of each file in the directory

# add a prefix to all filenames in the folder
prefix = "new_"
for file in p2.iterdir():
    if file.is_file():
        new_name = prefix + file.name
        new_path = file.with_name(new_name)
        file.rename(new_path)
        print(f"Renamed {file.name} to {new_name}")

# example usage of Path to iterate through all files in a directory (again)
p2=Path("files")
for file in p2.iterdir():
    print(file.name)  # print the name of each file in the directory

# remove the prefix from all filenames in the folder
for file in p2.iterdir():
    if file.is_file() and file.name.startswith(prefix):
        new_name = file.name[len(prefix):]
        new_path = file.with_name(new_name)
        file.rename(new_path)
        print(f"Renamed {file.name} to {new_name}")

# example usage of Path to iterate through all files in a directory (and again)
p2=Path("files")
for file in p2.iterdir():
    print(file.name)  # print the name of each file in the directory