from flask import Flask

app = Flask(__name__)

@app.route('/') # 'http://www.google.com/' Root

def home():
    return "Hello World!"

app.run(port=5000)