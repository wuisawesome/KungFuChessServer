Rules:

Pieces move the same as in normal chess.
Pieces have cooldown periods which vary based on piece.
You cannot interact with a piece while it is in transit.
Promotion is the same.
Multiple pieces can be in transit at once.
You cannot send multiple of your own pieces to the same square at once.


API:

/createGame
POST 
Parameters:
RoomName: str
secret: str (optional)
Returns:
JSON Object: {Error: ""} or {RoomName:str, player1 token: string, secret: string}

/joinGame
GET
Parameters:
RoomName: str
secret: str (optional)
Returns:
JSON Object: {Error: ""} or {player2 token: string}

/getGameState
Parameters:
GET
RoomName: str
Returns: 
{Board: int[][], inTransit: [(int, (int, int), (int, int), float)] -> [(piece, startpos, endpos, timelapsed), totalTime: long] 

/makeMove
POST
Parameters:
startPos: (int, int)
endPos: (int, int)
---or---
meta: enum
args: JSON
Returns:
{Error: str} or {success: True}


