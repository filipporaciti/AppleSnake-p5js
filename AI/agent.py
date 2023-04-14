from environment import Snake
import pymongo as pym
import numpy as np
import time


client = pym.MongoClient('localhost', 27017)
# client = pym.MongoClient('192.168.1.253', 27017)
db = client['snake']
collection = db['qtable']

gamma = 0.1
epsilon = 0.08

decay = 0.1


def getQtableValue(l, x, y, xm, ym):
    return collection.find_one({'l': int(l), 'x': int(x), 'y': int(y), 'xm': int(xm), 'ym': int(ym)})['action']
 
def setQtableValue(l, x, y, xm, ym, nl, nx, ny, nxm, nym, reward):
    newArray = getQtableValue(l, x, y, xm, ym)
    try:
        nextActions = getQtableValue(nl, nx, ny, nxm, nym)
        change = reward + gamma * max(nextActions)
    except:
        change = reward - 1000
    newArray[newArray.index(max(newArray))] = change
    collection.update_one({'l': l, 'x': x, 'y': y, 'xm': xm, 'ym': ym}, {'$set': {'action': newArray}})

for x in range(20):
    for y in range(19, 0, -1):
        print(x, y)
        buffer = []
        cont = True
        while cont:
            s = Snake(x, y)
            for i in range(150):
                pos = s.get_obs()
                act = 0
                
                
                if np.random.uniform() == epsilon:
                    act = np.random.choice(range(4))
                else:
                    act = getQtableValue(pos[0], pos[1], pos[2], pos[3], pos[4])
                    act = act.index(max(act))
                    
                reward, uscita = s.action(act)
                newPos = s.get_obs()
                
                setQtableValue(pos[0], pos[1], pos[2], pos[3], pos[4], newPos[0], newPos[1], newPos[2], newPos[3], newPos[4], reward)
                
                if not uscita:
                    print(reward, pos, act)
                    buffer.append(reward)
                    while len(buffer) > 20:
                        buffer.pop(0)
                    # if buffer.count(max(buffer)) == 15 and max(buffer) > 0:
                        
                    if buffer.count(max(buffer)) == 20:
                        if max(buffer) > 0:
                            cont = False
                        else:
                            for newx in range(20):
                                for newy in range(20):
                                    collection.update_one({'l': 1, 'x': newx, 'y': newy, 'xm': pos[3], 'ym': pos[4]}, {'$set': {'action': [np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()]}})
           
                        
                    break

        time.sleep(1)
        