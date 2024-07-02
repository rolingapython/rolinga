from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/",methods=['GET'])
def startingPoint():
    return jsonify({"response":"Test Ok"})

@app.route("/events",methods=['GET'])
def events():
    return jsonify({"events":[1,2,3,4,5]})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000, debug=True)