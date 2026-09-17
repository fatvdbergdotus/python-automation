import requests

# pip install filestack-python
from filestack import Client

filename = "https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3"

# download the file from the given URL and save it locally
response = requests.get(filename)
with open("Symphony_No_6_1st_movement.mp3", "wb") as file:
    file.write(response.content)
print("File downloaded and saved as Symphony_No_6_1st_movement.mp3")

# upload the file to a server (example)
url = "https://cgi-lib.berkeley.edu/ex/fup.cgi"
file = open('myfile.txt', 'rb')
# CURRENTLY NOT WORKING
#req = requests.post(url, files={"upfile":file})
#print(req.text)

# share a file with python and filestack
# create an account at filestack
client = Client('AcLSyQW80QWGoPtBcvXWgz')
new_filelink = client.upload(filepath='myfile.txt')
print(new_filelink.url)