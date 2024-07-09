from flask import Flask, jsonify, render_template, send_from_directory
from dataclasses import dataclass
from src.application.dto.NoticiasDTO import NoticiasDTO
from src.application.dto.EventDTO import EventDTO
from flask_mysqldb import MySQL
app = Flask(__name__, static_folder='static', static_url_path='')
mysql = MySQL(app)

app.config["MYSQL_HOST"] = "database"
app.config["MYSQL_USER"] = "user"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "mydatabase"

@app.route('/')
def index():
    return send_from_directory(app.static_url_path, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_url_path, path)

@app.route("/api/test",methods=['GET'])
def testPoint():
    return jsonify({"response":"Test Ok"})

@app.route("/api/events",methods=['GET'])
def events():
    sql = "SELECT id,name,location,description,image,link FROM events;"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    db_events = cursor.fetchall()    
    retorno = []
    for events in db_events:
        evento = EventDTO(
        name=events[1],
        location=events[2],
        description=events[3],
        image=events[4],
        link=events[5]
        )
        retorno.append(evento)
    cursor.close()    
    return jsonify({"data":retorno})

@app.route("/api/news",methods=['GET'])
def news():  
    sql = "SELECT id,title,image,description,link,publisher FROM News;"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    db_events = cursor.fetchall()    
    retorno = []
    for events in db_events:
        evento = NoticiasDTO(
        title=events[1],
        image=events[2],
        description=events[3],
        link=events[4],
        publisher=events[5]
        )
        retorno.append(evento)
    cursor.close()    
    return jsonify({"data":retorno})



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000, debug=True)