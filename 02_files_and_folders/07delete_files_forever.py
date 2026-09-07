from pathlib import Path

root_dir = Path("files_to_delete")
root_dir.mkdir(exist_ok=True)

# create files in the root dir
for filename in ["a", "b", "c"]:
    with open(root_dir / filename, "w") as file:
        file.write("empty")
        print("created " + str(root_dir / filename))

# permanently delete all files in the root_dir
for path in root_dir.glob("*"):
    with open(path, "wb") as file:
        file.write(b'')
    path.unlink()
    print("deleted " + str(path))
