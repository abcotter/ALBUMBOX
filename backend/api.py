from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Joy199731*MGMT2022"
app.config["MYSQL_DB"] = "postcardDB"

mysql = MySQL(app)


def get_post_data(name):
    data = request.get_json()
    value = data[name]
    return value


@app.route("/")
def hello_world():
    return "loser!"


@app.route("/getBoards", methods=["GET"])
def get_boards():
    res = []
    cur = mysql.connection.cursor()
    cur.execute("SELECT boardID, boardName FROM board")
    for board in cur:
        res.append({"id": board[0], "name": board[1]})
    return jsonify(res)


@app.route("/createBoard", methods=["POST"])
def create_board():
    param = get_post_data("name")
    sql = "INSERT INTO board (boardName) VALUES (%s);"
    cur = mysql.connection.cursor()
    cur.execute(sql, [param])
    mysql.connection.commit()
    cur.execute("select max(boardID) from board")
    row = cur.fetchone()[0]
    res = {"boardID": row, "boardName": param}
    return jsonify(res)


@app.route("/deleteBoard", methods=["POST"])
def delete_board():
    param = get_post_data("id")
    sql = "DELETE FROM board WHERE boardID = (%s);"
    cur = mysql.connection.cursor()
    cur.execute(sql, [param])
    sql = "DELETE FROM image_board WHERE boardID = (%s);"
    cur.execute(sql, [param])
    mysql.connection.commit()
    return jsonify("success")


@app.route("/getBoardImages", methods=["GET"])
def get_board_images():
    res = []
    param = request.args.get("boardId")
    sql = "SELECT image.imageID, image.altText, image.imageURL FROM image INNER JOIN image_board WHERE boardID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(sql, [param])
    for image in cur:
        res.append({"imageID": image[0], "altText": image[1], "URL": image[2]})
    return jsonify(res)
