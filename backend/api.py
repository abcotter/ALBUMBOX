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


def get_post_data(name):
    data = request.get_json()
    value = data[name]
    return(value)


@app.route('/')
def hello_world():
    return 'loser!'


@app.route('/getBoards', methods=['GET'])
def getBoards():
    res = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT boardID, boardName FROM board')
    for board in cur:
        res.append({
            'id': board[0],
            'name': board[1]
        })
    return jsonify(res)


@app.route('/createBoard', methods=['POST'])
def createBorad():
    param = get_post_data('name')
    sql = 'INSERT INTO board (boardName) VALUES (%s);'
    cur = mysql.connection.cursor()
    cur.execute(sql, [param])
    mysql.connection.commit()
    cur.execute("select max(boardID) from board")
    row = cur.fetchone()[0]
    res = [
        {'boardID': row, 'boardName': param}
    ]
    return jsonify(res)
