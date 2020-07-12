from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Joy199731*MGMT2022'
app.config['MYSQL_DB'] = 'postcardDB'

mysql = MySQL(app)


@app.route('/')
def hello_world():
    return 'loser!'


@app.route('/getBoards', methods=['GET'])
def getBoards():
    res = []
    cur = mysql.connection.cursor()
    cur.execute('''SELECT boardID, boardName FROM board''')
    for board in cur:
        res.append({
            'id': board.boardID,
            'name': board.boardName
        })
    return jsonify(res)


@app.route('/createBoard', methods=['POST'])
def createBorad():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)
