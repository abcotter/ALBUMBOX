from flask import Flask
app = Flask(__name__)

@app.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/')
def hello_world():
    return 'Hello, World!'