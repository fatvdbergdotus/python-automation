import fitz

with fitz.open("students.pdf") as file:
    for page in file:
        print(20*"-")
        text = page.get_text()
        print(text)
