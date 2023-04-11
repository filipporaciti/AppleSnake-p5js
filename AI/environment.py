import os
import time

import pymongo as pym
import numpy as np

import json

class Snake:
    def __init__(self, xm=0, ym=0):
        self.snake = [(10, 19), (10, 18), (10, 17)]
        self.apple = (xm, ym)
        self.reward = 0
        self.delay = 0.0
        
        
    def move(self, direction):
        x, y = self.snake[-1]
        if direction == 'u'or direction == 0:
            y -= 1
        elif direction == 'l'or direction == 1:
            x -= 1
        elif direction == 'd' or direction == 2:
            y += 1
        elif direction == 'r'or direction == 3:
            x += 1

        self.snake.append((x, y))    
        self.snake.pop(0) 
        
        
        if x > 19 or y > 19 or x < 0 or y < 0 or self.snake.count((x, y)) != 1:
            # Game over
            self.reward -= 100
            return False
        if (x, y) == self.apple:
            # Winnnn
            self.reward += 1000
            return False
        self.reward -= 1
        return True
    
    def show(self, epoca = 0):
        time.sleep(self.delay)
        try:
            os.system('clear')
            print(f"{epoca = } x:{self.snake[-1][0]} y: {self.snake[-1][1]}")
            area = [[0]*20 for _ in range(20)]
            area[self.apple[1]][self.apple[0]] = 1

            for piece in self.snake:
                area[piece[1]][piece[0]] = 1
                
            for i in range(20):
                print(' '.join(map(str, area[i])))
                
        # except IndexError:
        #     # Game over
        #     self.reward -= 100 
        #     return False 
        except Exception as e:
            print('errore showwww: ' + str(e))

        return True
        
            
    def get_obs(self):
        return (1, 1)[1:] + self.snake[-1] + self.apple
    
    def action(self, action, show=False, ephoc=None):
        out = self.move(action)
        if show:
            self.show(ephoc)
        return self.reward, out