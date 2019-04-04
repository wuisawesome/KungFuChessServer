from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/createGame", methods=['POST'])
def createGame(roomName, secret=""):
    return {
            "roomName": roomName,
            "player1": "Timothy Liu",
            "secret": secret
            }

@app.route("/joinGame", methods=['POST'])
def joinGame(roomName, secret=""):
    pass

@app.route("/getGameState", methods=['GET'])
def getGameState(roomName):
    pass

@app.route("/makeMove", methods=['POST'])
def makeMove(startPos, endPos):
    pass


