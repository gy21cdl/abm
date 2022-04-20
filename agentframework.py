# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:36:52 2022

@author: clambert
"""

#Imported modules
import random


#Define "Agent" class
class Agent():
    
    #generate random x & y values
    def __init__ (self):
        """
        __init__ creates random starting values for x & y between 0 and 99.

        Returns random starting values
        -------
        
        """
        self.x = random.randint (0,99)
        self.y = random.randint (0,99)
        #print (self.x) # test
        #print (self.y) # test
    
    #moves the agents
    def move (self):
        """
        move takes the values generated in __init__ and moves them one step

        Returns new values moved by one step
        -------
        
        """
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:       
            self.y = (self.y - 1) % 100

    pass

