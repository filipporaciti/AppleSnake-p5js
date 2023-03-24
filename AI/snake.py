import os
import time

import pymongo as pym
import numpy as np

import json

client = pym.MongoClient('192.168.1.253', 27017)
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


snake = [(10, 19), (10, 18), (10, 17)]

apple = (10, 10)

    
def show():
    try:
        time.sleep(0.2)
        os.system('cls')
        area = [[0]*20 for _ in range(20)]
        area[apple[1]][apple[0]] = 1

        for piece in snake:
            assert piece[1] >= 0 and piece[0] >= 0
            area[piece[1]][piece[0]] = 1
            
        for i in range(20):
            print(' '.join(map(str, area[i])))
    except: #IndexError
        gameOver()
    
    
def sendInfo(reward):
    1    
    

        
def win():
    for piece in snake:
        if piece == apple:
            print('Win')
            sendInfo(1000)
            exit()
    
    
    
def gameOver():
    print('Game over')
    sendInfo(-100)
    exit()
        
        
def move(direction):
    x, y = snake[-1]
    if direction == 'u':
        y -= 1
    elif direction == 'l':
        x -= 1
    elif direction == 'd':
        y += 1
    elif direction == 'r':
        x += 1
        
    snake.append((x, y))    
    snake.pop(0) 


show()
for _ in range(100):
    move('u')
    show()
    win()
    

