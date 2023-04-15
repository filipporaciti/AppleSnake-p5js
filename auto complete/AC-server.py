import pymongo as pym
import numpy as np

import json

import socket

from flask_cors import CORS
from flask import Flask, request, jsonify
app = Flask(__name__)
cors = CORS(app)


def createDataTable(xm, ym):
    data = [[0 for _ in range(20)] for _ in range(20)]
    data[ym][xm] = 100

    xt = xm+1
    value = 99
    while xt < 20:
        data[ym][xt] = value
        value -= 1
        xt += 1
    xt = xm-1
    value = 99
    while xt >= 0:
        data[ym][xt] = value
        value -= 1
        xt -= 1
    yt = ym-1
    value = 99
    while yt >= 0:
        data[yt][xm] = value
        value -= 1
        yt -= 1
    yt = ym+1
    value = 99
    while yt < 20:
        data[yt][xm] = value
        value -= 1
        yt += 1
    for d in data:
        if 0 in d:
            ym = data.index(d)
            value = max(d)
            xt = d.index(value)+1
            while xt < 20:
                data[ym][xt] = value-1
                value -= 1
                xt += 1
            value = max(d)
            xt = d.index(value)-1
            while xt >= 0:
                data[ym][xt] = value-1
                value -= 1
                xt -= 1
    return data
                

@app.route('/getAction', methods = ['GET'])
def getAction():
    try:
        l = int(request.args.get('l'))
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        xm = int(request.args.get('xm'))
        ym = int(request.args.get('ym'))
        
        data = createDataTable(xm, ym)
        
        a = [data[y-1][x], data[y][x-1], data[y+1][x], data[y][x+1]]
        
        action = a.index(max(a))
                
            
        return jsonify({'action': action})
    except Exception as e:
        print(e)
        return '{"action": "Errore getAction"}'
    



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

app.run(host=ip, port=8081)