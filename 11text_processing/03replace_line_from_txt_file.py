

# replace a specific line in one specific text file
line_number_to_replace = 2  # line numbers start from 1
new_line_content = "This is the new content for line number " + str(line_number_to_replace) + ".\n"
input_file_path = "file_with_multiple_lines.txt"

with open(input_file_path, "r+") as file:
    # start by reading all lines from the file
    lines = file.readlines()
    if 0 < line_number_to_replace <= len(lines):
        # replace the specified line with the new content
        lines[line_number_to_replace - 1] = new_line_content
        file.seek(0)
        file.writelines(lines)
        file.truncate()
        print("contents of", input_file_path, "after replacement:\n", "".join(lines))