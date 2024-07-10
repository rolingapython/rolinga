from flask import Flask, jsonify, render_template, send_from_directory, request,redirect, url_for
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
def default_page():
    return redirect(url_for('static', filename='index.html'))

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
        id = events[0],
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
        id = events[0],
        title=events[1],
        image=events[2],
        description=events[3],
        link=events[4],
        publisher=events[5]
        )
        retorno.append(evento)
    cursor.close()    
    return jsonify({"data":retorno})


@app.route('/api/createnews', methods=['POST'])
def createnews():
    data = request.json
    event_dto = EventDTO(
        id =0,
        name=data.get('name'),  
        location=data.get('location'),
        description=data.get('description'),
        image=data.get('image'),
        link=data.get('link')
    )
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO events (name, location, description, image, link) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (event_dto.name, event_dto.location, event_dto.description, event_dto.image, event_dto.link))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Evento creado correctamente'})

@app.route('/api/updatenews/<int:id>', methods=['PUT'])
def updatenews(id):
    data = request.json
    cursor = mysql.connection.cursor()
    sql = """
    UPDATE events 
    SET name = %s, location = %s, description = %s, image = %s, link = %s 
    WHERE id = %s
    """
    result = cursor.execute(sql, (
        data.get('name'),
        data.get('location'),
        data.get('description'),
        data.get('image'),
        data.get('link'),
        id
    ))
    mysql.connection.commit()
    cursor.close()
    if result:
        return jsonify({'message': f'Evento con ID {id} actualizado correctamente'})
    else:
        return jsonify({'message': f'No se encontró un evento con ID {id}'}), 404



@app.route('/api/deletenews/<int:id>', methods=['DELETE'])
def deletenews(id):
    cursor = mysql.connection.cursor()
    sql = "DELETE FROM events WHERE id = %s"
    result = cursor.execute(sql, (id,))
    mysql.connection.commit()
    cursor.close()
    if result:
        return jsonify({'message': f'Evento con ID {id} eliminado correctamente'})
    else:
        return jsonify({'message': f'No se encontró un evento con ID {id}'}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000, debug=False)