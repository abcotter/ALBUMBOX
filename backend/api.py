from flask import Flask, request, jsonify, make_response, send_file
from flask_mysqldb import MySQL
from flask_cors import CORS
from base64 import b64encode
import io, os, glob

app = Flask(__name__, static_url_path="/static")
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
    fileType = data["fileType"]
    memDate = data["memDate"]
    memDescription = data["memDescription"]
    if memDescription == "null":
        memDescription = ""
    altText = data["altText"]
    boardId = data["boardId"]
    params = (altText, memDate, fileType, memDescription)
    sql = "INSERT INTO image (altText, memDate, fileType, memDesciption) VALUES (%s, %s, %s, %s); SELECT LAST_INSERT_ID();"
    connection = mysql.connection
    cur = connection.cursor()
    cur.execute(sql, params)
    row = connection.insert_id()
    imageFile.save(f"static/images/{row}.{fileType}")
    params = (row, boardId)
    sql = "INSERT INTO image_board (imageID, boardID) VALUES (%s, %s)"
    cur.execute(sql, params)
    mysql.connection.commit()
    return jsonify(row)


@app.route("/createAccount", methods=["POST"])
def create_account():
    sql = "SELECT email FROM user WHERE email=%s"
    params = (get_post_data("email"),)
    cur = mysql.connection.cursor()
    cur.execute(sql, params)
    result = cur.fetchone()
    print("result")
    print(result)
    if result:
        return jsonify(message="A user with this e-mail already exists."), 401
    else:
        params = (
            get_post_data("email"),
            get_post_data("password"),
            get_post_data("name"),
        )
        sql = "INSERT INTO user (email, password, name) VALUES (%s, %s, %s);"
        cur.execute(sql, params)
        mysql.connection.commit()
        return jsonify("success"), 200


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
    cur = mysql.connection.cursor()
    param = get_post_data("id")
    sql = "SELECT imageID FROM image_board WHERE boardID = %s;"
    cur.execute(sql, [param])
    print(len(cur.fetchall()))
    images = cur.fetchall()[0] if len(cur.fetchall()) > 0 else []
    if len(images) == 1:
        sql = "DELETE FROM image WHERE imageID = %s"
        cur.execute(sql, images)
    elif len(images) > 1:
        sql = "DELETE FROM image WHERE imageID IN %s"
        cur.execute(sql, images)
    if len(images) >= 1:
        for image in images:
            path = glob.glob(f"static/images/{image}.*")[0]
            if os.path.exists(path):
                os.remove(path)
    sql = "DELETE FROM board WHERE boardID = (%s);"
    cur.execute(sql, [param])
    sql = "DELETE FROM image_board WHERE boardID = (%s);"
    cur.execute(sql, [param])
    mysql.connection.commit()
    return jsonify("success")


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    cur = mysql.connection.cursor()
    param = get_post_data("id")
    print(param)
    sql = "DELETE FROM image WHERE imageID = %s"
    cur.execute(sql, [param])
    path = glob.glob(f"static/images/{param}.*")[0]
    if os.path.exists(path):
        os.remove(path)
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


@app.route("/editImage", methods=["POST"])
def edit_image():
    data = request.form.to_dict()
    imageId = data["imageID"]
    memDescription = data["memDescription"]
    cur = mysql.connection.cursor()
    params = (memDescription, imageId)
    sql = "UPDATE image SET memDesciption = %s WHERE imageID = %s;"
    cur.execute(sql, params)
    mysql.connection.commit()
    return jsonify("success")


@app.route("/getBoardImages", methods=["GET"])
def get_board_images():
    res = []
    param = request.args.get("boardId")
    sql = "SELECT image.imageID, image.altText, image.memDate, image.fileType, image.memDesciption FROM image INNER JOIN image_board ON image.imageID = image_board.imageID WHERE image_board.boardID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(sql, [param])
    for image in cur:
        res.append(
            {
                "imageID": image[0],
                "altText": image[1],
                "date": image[2],
                "description": image[4],
                "imageURL": f"http://127.0.0.1:5000/static/images/{image[0]}.{image[3]}",
            }
        )
    return jsonify(res)
