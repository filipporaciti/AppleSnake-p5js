import os
import time

import pymongo as pym
import numpy as np

import json

client = pym.MongoClient('localhost', 27017)
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
       

       
def getQtableValue(l, x, y, xm, ym):
    return collection.find_one({'l': int(l), 'x': int(x), 'y': int(y), 'xm': int(xm), 'ym': int(ym)})['action']
 
def setQtableValue(l, x, y, xm, ym, nl, nx, ny, nxm, nym, reward):

    nextActions = getQtableValue(nl, nx, ny, nxm, nym)
    change = reward + gamma * max(nextActions)
    newArray = getQtableValue(l, x, y, xm, ym)
    newArray[newArray.index(max(newArray))] = change
    collection.update_one({'l': l, 'x': x, 'y': y, 'xm': xm, 'ym': ym}, {'$set': {'action': newArray}})    
    # print(newArray)
    # print(change)
    # print(nextActions)
    # print(snake)
    

    
#epochs = 200
gamma = 0.1
epsilon = 0.08
decay = 0.1

reward = 0

noEnd = True

snake = [(10, 19), (10, 18), (10, 17)]

apple = (10, 14)

    
def show(epoca = 0):
    try:
        os.system('clear')
        print(f"{epoca = } x:{snake[-1][0]} y: {snake[-1][1]}")
        area = [[0]*20 for _ in range(20)]
        area[apple[1]][apple[0]] = 1

        for piece in snake:
            # if snake.count(piece) != 1:
            #     gameOver()
            #     return False
            area[piece[1]][piece[0]] = 1
            
        for i in range(20):
            print(' '.join(map(str, area[i])))
            
    except IndexError:
        gameOver()  
        return False 
    except:
        print('altro errore')
        exit()

    return True
    

        
def win():
    for piece in snake:
        if piece == apple:
            print('Win')
            global reward
            reward += 1000
            return False
    
    
    
def gameOver():
    global reward
    reward -= 100
    
        
        
def move(direction):
    x, y = snake[-1]
    if direction == 'u'or direction == 0:
        y -= 1
    elif direction == 'l'or direction == 1:
        x -= 1
    elif direction == 'd' or direction == 2:
        y += 1
    elif direction == 'r'or direction == 3:
        x += 1
    else:
        return False
    if x > 19 or y > 19 or x < 0 or y < 0:
        gameOver()
        return False
        
    snake.append((x, y))    
    snake.pop(0) 
    global reward
    reward -= 1
    return True


while True:
    show()
    for epoca in range(100):
        x = snake[-1][0]
        y = snake[-1][1]
        xm = apple[0]
        ym = apple[1]
        d = 0
        
        if np.random.uniform() < epsilon:
            d = np.random.choice(range(4))
        else:
            d = getQtableValue(1, x, y, xm, ym)
            d = d.index(max(d))
        
        noEnd = move(d)
        
        noEnd = show(epoca)
        noEnd = win()
        
        nx = snake[-1][0]
        ny = snake[-1][1]
        
        setQtableValue(1, x, y, xm, ym, 1, nx, ny, xm, ym, reward)
        
        if noEnd == False or epoca >= 99:
            os.system('clear')
            print('Exittttttt')
            print(f"{snake = }")
            print(f"{apple = }")
            print(f"{reward = }")
            print(x, y, nx, ny)
            time.sleep(2)
            reward = 0
            noEnd = True
            snake = [(10, 19), (10, 18), (10, 17)]

        
        time.sleep(0.1)
