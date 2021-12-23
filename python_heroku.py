import flask
import os
from flask import jsonify, request
import json
response = ''
app = flask.Flask(__name__)

@app.route('/dir')
def favicon():
    return "Hoşgeldiniz"

@app.route('/name', methods = ["GET"])
def nameRoute():
    postdata = request.args.get("aa")
    #creds = json.loads(postdata)
    print(postdata)
    return postdata

        
@app.route("/authenticate", methods  = ["POST"])
def authenticate():
    postdata = request.args.get()
    creds = json.loads(postdata)
    print(creds)


@app.route('/home')
def home():
    return "Hello World"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()



    # #fetching the global response variable to manipulate inside the function
    # global response
    # d = {}
    # user = str(request.args['query'])
    # answer = str((user))
    # d['output'] = answer
    # return d