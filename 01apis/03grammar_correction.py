import requests

url = "https://api.languagetoolplus.com/v2/check"
data = {
    "text": "This is a exemple sentence with a error.",
    "language": "auto",
}

response = requests.post(url, data=data)
content = response.json()

for match in content["matches"]:
    print(f"Error: {match['message']}")
    print(f"Context: {match['context']['text']}")
    print(f"Suggested correction: {match['replacements'][0]['value']}")
    print(20*"-")
