from databaseFunc import databaseNeeds
from pymongo import MongoClient

from flask import Flask, request
app = Flask(__name__)


@app.route('/distance/', methods=["GET","POST"])
def distanceHTTP():

    if request.method == 'GET':
        return '', 200
    elif request.method == 'POST':
        return '', 200
    else:
        return '', 500

@app.route("/retirement/",methods=["GET","POST"])
def retirementHTTP():
    if request.method == 'GET':
        return '', 200
    elif request.method == 'POST':
        return '', 200
    else:
        return '', 500

if __name__ == "__main__":
    app.run()