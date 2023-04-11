import pymongo as pym
import numpy as np

import json

import socket
from flask_cors import CORS
from flask import Flask, request, jsonify
app = Flask(__name__)
cors = CORS(app)

# client = pym.MongoClient('192.168.1.253', 27017)
client = pym.MongoClient('localhost', 27017)
db = client['snake']
collection = db['qtable']


# Insert all data
# for l in range(1, 11):
#     print(l)
#     for x in range(20):
#         for y in range(20):
#             for xm in range(20):
#                 for ym in range(20):
#                     collection.insert_one({'l': l, 'x': x, 'y': y, 'xm': xm, 'ym': ym, 'action': [np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()]})
           


def getQtableValue(l, x, y, xm, ym):
    return collection.find_one({'l': int(l), 'x': int(x), 'y': int(y), 'xm': int(xm), 'ym': int(ym)})['action']
 
def setQtableValue(l, x, y, xm, ym, nl, nx, ny, nxm, nym, reward):
    try:
        nextActions = getQtableValue(nl, nx, ny, nxm, nym)
        change = reward + gamma * max(nextActions)
        newArray = nextActions
        newArray[newArray.index(max(nextActions))] = change
        collection.update_one({'l': l, 'x': x, 'y': y, 'xm': xm, 'ym': ym}, {'$set': {'action': newArray}})    
        return True
    except:
        return False          
                    
#epochs = 200
gamma = 0.1
epsilon = 0.08
decay = 0.1


# if np.random.uniform() < epsilon:
#             action = np.random.choice(range(4))
# else:
#     actions = getQtableValue(1, 0, 0, 1, 1)
#     action = max(actions)

# reward = 100
# actions[actions.index(action)] = reward + gamma * action
# setQtableValue(1, 0, 0, 1, 1, actions)


@app.route('/getAction', methods = ['GET'])
def getAction():
    try:
        l = request.args.get('l')
        x = request.args.get('x')
        y = request.args.get('y')
        xm = request.args.get('xm')
        ym = request.args.get('ym')
        
        
        if np.random.uniform() < epsilon:
            action = np.random.choice(range(4))
        else:
            actions = getQtableValue(l, x, y, xm, ym)
            action = actions.index(max(actions))
            
        return jsonify({'action': action})
    except Exception as e:
        print(e)
        return '{"action": "Errore getAction"}'
    
@app.route('/setAction', methods = ['POST'])
def setAction():
    try:

        l = request.json.get('l')
        x = request.json.get('x')
        y = request.json.get('y')
        xm = request.json.get('xm')
        ym = request.json.get('ym')
        
        nl = request.json.get('nl')
        nx = request.json.get('nx')
        ny = request.json.get('ny')
        nxm = request.json.get('nxm')
        nym = request.json.get('nym')
        
        reward = request.json.get('reward')
        
        print(l, x, y, xm, ym, nl, nx, ny, nxm, nym, reward)
            
        return str(setQtableValue(l, x, y, xm, ym, nl, nx, ny, nxm, nym, reward))
    except Exception as e:
        print(e)
        return '{"action": "Errore setAction"}'




s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

app.run(host=ip, port=8081)