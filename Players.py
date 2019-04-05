players = {}

playerStats = {
    "name": "",
    "correct": 0,
}

board = []

def addPlayer(name):
    if name in players:
        return "Already Exists, choose another!"
    else:
        newPlayer = playerStats
        newPlayer["name"] = name
        players[name] = newPlayer
        board.append(newPlayer)
    return newPlayer

def remove(name):
    return name

def updateBoard():
    return 1