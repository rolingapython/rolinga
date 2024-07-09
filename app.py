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

    db_peliculas = cursor.fetchall()
    
    retorno = []
    for pelicula in db_peliculas:
        evento = EventDTO(
        name=pelicula[1],
        location=pelicula[2],
        description=pelicula[3],
        image=pelicula[4],
        link=pelicula[5]
        )
        retorno.append(evento)

    cursor.close()

    
    return jsonify({"data":retorno})

@app.route("/api/news",methods=['GET'])
def news():  
    retorno = [
    NoticiasDTO(title="Noticia 1",image="imagen1.jpg",description="Descripción de la noticia 1",link="http://enlace1.com",publisher="Publicador 1"),
    NoticiasDTO(title="Noticia 2",image="imagen2.jpg",description="Descripción de la noticia 2", link="http://enlace2.com",publisher="Publicador 2"),
    NoticiasDTO(title="Noticia 3",image="imagen3.jpg",description="Descripción de la noticia 3",link="http://enlace3.com",publisher="Publicador 3")
    ]
    return jsonify({"data":retorno})



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000, debug=True)