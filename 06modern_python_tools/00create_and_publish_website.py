from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

app.run(host='0.0.0.0')

# see an online version at:
# https://freekvdb.pythonanywhere.com/
