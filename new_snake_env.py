#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:55:18 2021

@author: dayman

Updated snake_env
"""

import numpy as np
import pygame as pg

class snake_game:
    def __init__(self):
        self.snake = snake()
        pass
    
    def init_render:
        """
        Start pygame to potentially render game
        """
        pass
    
    def render:
        """
        Rendering game for human players or reviewing
        """
        pass
    
    def step:
        """
        Func. to step game one frame
        """
        
        snake
        
        pass
    
    
class snake:
    def __init__(self):
        self.head = [0,0] # Position of the head
        self.blocks = [[headx, heady]]
        self.direction = np.array([1,0])
        self.speed = 10 # coordnates/frame
        self.eaten = False
        
    def move(self):
        self.head = self.head + self.direction*self.speed
        blocks.append(self.append)
        
        if not eaten:
            self.blocks.pop(0) # if not eaten, does not get further
    
    
        
        
class food:
    def __init__(self):
        pass
    
    