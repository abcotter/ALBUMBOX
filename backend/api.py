from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1.3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Joy199731*MGMT2022'
app.config['MYSQL_DB'] = 'postcarDB'

mysql = MySQL(app)

@app.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/')
def hello_world():
    return 'loser!'