import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS
CORS(app)
# sanity check route
@app.route('/index', methods=['GET'])
def main():
    return jsonify('Hello World')


@app.route('/join', methods=['POST'])
def add_user():
    name = request.json['name']
    f = open('data.txt', 'a')
    f.write(str(name)+'\n')
    return 'join'
@app.route('/leave', methods=['POST'])
def remove_user():
    name = request.json['name']
    f = open("data.txt","r")
    lines = f.readlines()
    f.close()
    f = open("data.txt","w")
    for line in lines:
        if line!=name+"\n":
            f.write(line)

    return 'leave'
@app.route('/players', methods= ['GET'])
def players():
    f = open('data.txt',"r")
    lines = f.read().splitlines()
    return jsonify(lines)

if __name__ == "__main__":
    app.run(debug=True)