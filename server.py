''' 
docker run --name tetrisMongo -p 27017:27017 -dit mongo
{
    nome: "pippo",
    punti: 0
}
'''

import pymongo as pym
import json, socket


from flask_cors import CORS
from flask import Flask, request
app = Flask(__name__)
cors = CORS(app)

client = pym.MongoClient('192.168.1.253', 27017)
db = client['snake']
collection = db['classifica']


def getData():
    return collection.find()


def insertScore(nome, score):
    
    try:
        data = getData()
        
        for x in data:
            if nome == x['nome']:
                collection.update_one({'nome': nome}, {'$set':{'score': score}})
                return
        
        newData = {"nome": nome, "score": int(score)}
        collection.insert_one(newData)
    except:
        return -1



def getFirstTen():
    data = list(collection.find().sort('score', pym.DESCENDING).limit(10))
    return data
    




@app.route('/visualizza_classifica',methods = ['GET'])
def visualizza_classifica():
    
    try:
        return getFirstTen()
    except Exception as e:
        print(e)
        return '{"Error": "Errore visualizzazione classifica"}'



@app.route('/add_score',methods = ['POST'])
def add_score():
    
    data = request.get_json()
    
    try:
        insertScore(data['nome'], int(data['score']))
        return '{"info": "Score aggiunto"}'
    except Exception as e:
        print(e)
        return '{"Error": "Errore score"}'





s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()


app.run(host=ip, port=8081)