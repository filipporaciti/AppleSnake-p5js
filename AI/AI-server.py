import pymongo as pym
import numpy as np

import json

import socket
from flask_cors import CORS
from flask import Flask, request, jsonify
app = Flask(__name__)
cors = CORS(app)

client = pym.MongoClient('192.168.1.253', 27017)
# client = pym.MongoClient('localhost', 27017)
db = client['snake']
collection = db['qtable']


# Insert all data
# for l in range(1, 2):
#     print(l)
#     for x in range(20):
#         for y in range(20):
#             for xm in range(20):
#                 for ym in range(20):
#                     collection.insert_one({'l': l, 'x': x, 'y': y, 'xm': xm, 'ym': ym, 'action': [np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()]})
# exit()

def getQtableValue(l, x, y, xm, ym):
    return collection.find_one({'l': int(l), 'x': int(x), 'y': int(y), 'xm': int(xm), 'ym': int(ym)})['action']


@app.route('/getAction', methods = ['GET'])
def getAction():
    try:
        l = request.args.get('l')
        x = request.args.get('x')
        y = request.args.get('y')
        xm = request.args.get('xm')
        ym = request.args.get('ym')
        
        
    
        actions = getQtableValue(l, x, y, xm, ym)
        action = actions.index(max(actions))
            
        return jsonify({'action': action})
    except Exception as e:
        print(e)
        return '{"action": "Errore getAction"}'
    



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

app.run(host=ip, port=8081)