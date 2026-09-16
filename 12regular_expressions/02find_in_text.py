import re

data=[
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com", 
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants"
]

# Print all entries in the data
print("All entries:")
for entry in data:
    print(entry)

# Example: find all entries that contain Delhi in the data
pattern = re.compile(r"Delhi", re.IGNORECASE)
delhi_entries = [entry for entry in data if pattern.search(entry)]

print("\nEntries containing Delhi:")
for entry in delhi_entries:
    print(entry)

# Example: find all entries that contain Delhi and an email address in the data
pattern = re.compile(r"Delhi.*\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", re.IGNORECASE)
delhi_email_entries = [entry for entry in data if pattern.search(entry)]

print("\nEntries containing Delhi and an email address:")
for entry in delhi_email_entries:
    print(entry)

# Example: find all entries that contain Delhi and a phone number
pattern = re.compile(r"Delhi.*\+?\d{7,}", re.IGNORECASE)
delhi_phone_entries = [entry for entry in data if pattern.search(entry)]

print("\nEntries containing Delhi and a phone number:")
for entry in delhi_phone_entries:
    print(entry)

# Example: find all entries that contain a phone number and email address
pattern = re.compile(r"\+?\d{7,}.*\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", re.IGNORECASE)
phone_email_entries = [entry for entry in data if pattern.search(entry)]

print("\nEntries containing a phone number and an email address:")
for entry in phone_email_entries:
    print(entry)