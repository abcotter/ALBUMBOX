from flask import Flask, request, jsonify, make_response, send_file
from flask_mysqldb import MySQL
from flask_cors import CORS
from base64 import b64encode
import io

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


@app.route("/addImage", methods=["POST"])
def add_image():
    data = request.form.to_dict()
    imageFile = request.files["file"]
    memDate = data["memDate"]
    memDescription = data["memDescription"]
    altText = data["altText"]
    boardId = data["boardId"]
    params = (altText, imageFile, memDate, memDescription)
    sql = "INSERT INTO image (altText, imageFile, memDate, memDesciption) VALUES (%s, %b, %s, %s); SELECT LAST_INSERT_ID();"
    connection = mysql.connection
    cur = connection.cursor()
    cur.execute(sql, params)
    row = connection.insert_id()
    imageFile.save(f"static/images/{row}.jpeg")
    params = (row, boardId)
    sql = "INSERT INTO image_board (imageID, boardID) VALUES (%s, %s)"
    cur.execute(sql, params)
    mysql.connection.commit()
    return jsonify("success")


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


@app.route("/getBoards", methods=["GET"])
def get_boards():
    res = []
    cur = mysql.connection.cursor()
    cur.execute("SELECT boardID, boardName FROM board")
    for board in cur:
        res.append({"id": board[0], "name": board[1]})
    return jsonify(res)


@app.route("/getBoardImages", methods=["GET"])
def get_board_images():
    res = []
    param = request.args.get("boardId")
    sql = "SELECT image.imageID, image.altText, image.memDate, image.memDesciption FROM image INNER JOIN image_board ON image.imageID = image_board.imageID WHERE image_board.boardID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(sql, [param])
    for image in cur:
        res.append(
            {
                "imageID": image[0],
                "altText": image[1],
                "date": image[2],
                "description": image[3],
            }
        )
    return jsonify(res)


@app.route("/getImage", methods=["GET"])
def getimage():
    param = request.args.get("imageID")
    sql = "SELECT image.imageFile FROM image WHERE imageID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(sql, [param])
    res = cur.fetchone()[0]
    image = b64encode(res).decode("utf-8")
    response = make_response(image)
    response.headers.set("Content-Type", "image/jpeg")
    print(response)
    return send_file(
        io.BytesIO(image),
        mimetype="image/jpeg",
        as_attachment=False,
        attachment_filename="%s.jpg" % param,
    )
