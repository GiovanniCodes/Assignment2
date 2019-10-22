from databaseFunc import databaseNeeds
from pymongo import MongoClient

from flask import Flask, request
client = MongoClient("mongodb://localhost:27017/")
db = client.assign2
results = db["results"]
entries = db["entries"]
requestIn = db["request"]


app = Flask(__name__)


@app.route('/distance/', methods=["GET","POST"])
def distanceHTTP():

    allDistData = ''
    databaseNeeds.insertRequest("localhost:27017/distance")
    for document in entries.find({}, {"_id": 0, "x1": 1, "x2": 1, 'y1': 1, "y2": 1, "timestamp": 1}):
        tempRetire = str(document)
        if (len(document) == 0):
            continue
        else:
            allDistData = allDistData + tempRetire

    if request.method == 'GET':
        return allDistData
    else:
        return "Made a Post Request"

@app.route("/retirement/",methods=["GET","POST"])
def retirementHTTP():

    allRetireData = ''
    databaseNeeds.insertRequest("localhost:27017/retirement")
    for document in entries.find({}, {"_id": 0, "age": 1, "annualSalary": 1, 'percentSaved': 1,"retirementSaveGoal": 1}):
        tempRetire = str(document)
        if (len(document) == 0):
            continue
        else:
            allRetireData = allRetireData + tempRetire

    if request.method == 'GET':
        return allRetireData
    elif request.method == 'POST':
        return "Made a Post Request"


if __name__ == "__main__":
    app.run()