import json

# Function to get the definition of a word from the dictionary.json file
def get_definitions(word):
    data = json.load(open("dictionary.json"))
    return data.get(word.lower(), "Word not found")

# Example usage
input_word = input("Enter a word (for instance Island): ")
for index, definition in enumerate(get_definitions(input_word)):
    print(f"{index + 1}. {definition}")