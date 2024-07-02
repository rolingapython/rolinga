from flask import Flask, jsonify, render_template, send_from_directory


app = Flask(__name__, static_folder='static', static_url_path='')

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
    return jsonify({"events":[1,2,3,4,5]})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000, debug=True)