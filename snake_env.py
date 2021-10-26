# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:08:42 2020

@author: karlm
"""

import pygame as pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (255, 255, 255)

# Display width and height
x = 500
y = 500

# Pictures used for joke version of game
ol = pygame.image.load('ol.jpg')
michael = pygame.image.load('michael.png')
karsten = pygame.image.load('karsten.png')

# Resize pictures
michael = pygame.transform.scale(michael, (50, 50))
ol = pygame.transform.scale(ol,(50,50))
karsten = pygame.transform.scale(karsten, (50, 50))

# Starting position of snake
x1 = 250        
y1 = 250

# Speed of snake
x1_change = 0
y1_change = 0

snake = [x1, y1, 2, 2]

# Init display
dis = pygame.display.set_mode((x, y))
pygame.display.set_caption("Scuffed Snake gaem")

clock = pygame.time.Clock()

# Two types of fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Location of food
food_x = 0
food_y = 0

# Func to spawn new food within display
def new_food():
    food_x = random.randint(0, (x - 10) / 10) * 10
    food_y = random.randint(0, (y - 10) / 10) * 10
    return food_y, food_x

# Func to draw the at current coordinates
def draw_snake(snake_coords):
    for i in snake_coords:
        # If snake head, draw different color
        if i == snake_coords[-1]:
            pygame.draw.rect(dis, red, [i[0], i[1], 10, 10])
        else:
            pygame.draw.rect(dis, black, [i[0], i[1], 10, 10])

# Func to draw Michael pic instead
def draw_michael(snake_coords):
    for r, i in enumerate(snake_coords):
        if i == snake_coords[-1]:
            dis.blit(michael, (i[0],i[1]))
        else:
            dis.blit(karsten, (i[0],i[1]))

def death():
    game_on = False

food_x, food_y = new_food()

snake_blocks = []
length_of_snake = 1

elapsed_time = 0

superchargedX = False
superchargedY = False

game_on = True

def play_game():
    while game_on == True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
                
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
                
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
                
            elif event.key == pygame.K_c:
                food_y, food_x = new_food()
                print("C")
                print(food_x, food_y)
    
    if y1 > y:
        y1_change = -50
        superchargedY = True
    if y1 < 0:
        y1_change = 50
        superchargedY = True
  
    if x1 > x:
        x1_change = -50
        superchargedX = True
        
    if x1 < 0:
        x1_change = 50
        superchargedX = True
    
    # If the snake has eaten food
    if y1 == food_y and x1 == food_x:
        elapsed_time = 0
        print("Yeds")
        food_x, food_y = new_food()
        length_of_snake += 1
        
    if elapsed_time > 5000:
        elapsed_time = 0
        print("Non")
        food_x, food_y = new_food()
        length_of_snake += -1
        
        if length_of_snake == 0:
            death()
        
        
    # Move x coordinates depending on current speed
    x1 += x1_change
    y1 += y1_change
    
    # Append the snake head to the current blocks
    snake_head = [x1, y1]
    snake_blocks.append(snake_head)
    
    # Delete last block of the snake
    if len(snake_blocks) > length_of_snake:
        del snake_blocks[0]
    
    # Check if any of the non-head snake blocks intersect with the head
    for i in snake_blocks[0:-1]:
        if i == snake_head:
            print("u suck")
    
    # Draw the snake, either as michael or normal snake
    draw_snake(snake_blocks)
    #draw_michael(snake_blocks)
    
    # Draw the food either as normal food or as beer
    pygame.draw.rect(dis, green, [food_x, food_y, 10, 10])
    #dis.blit(ol, (food_x, food_y))
    
    # To move the snanke back if it hits the border
    if superchargedX == True:
        x1_change = 10
        superchargedX = False
        print("SuperX")
    
    if superchargedY == True:
        y1_change = 10
        superchargedY = False
        print("SUPERY")
    
    
    et = clock.tick(10)
    elapsed_time += et
    print(elapsed_time)
    
    pygame.display.update()
    
    
    dis.fill(white)

while game_on == True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
                
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
                
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
                
            elif event.key == pygame.K_c:
                food_y, food_x = new_food()
                print("C")
                print(food_x, food_y)
    
    if y1 > y:
        y1_change = -50
        superchargedY = True
    if y1 < 0:
        y1_change = 50
        superchargedY = True
  
    if x1 > x:
        x1_change = -50
        superchargedX = True
        
    if x1 < 0:
        x1_change = 50
        superchargedX = True
    
    # If the snake has eaten food
    if y1 == food_y and x1 == food_x:
        elapsed_time = 0
        print("Yeds")
        food_x, food_y = new_food()
        length_of_snake += 1
        
    if elapsed_time > 5000:
        elapsed_time = 0
        print("Non")
        food_x, food_y = new_food()
        length_of_snake += -1
        
        if length_of_snake == 0:
            death()
        
        
    # Move x coordinates depending on current speed
    x1 += x1_change
    y1 += y1_change
    
    # Append the snake head to the current blocks
    snake_head = [x1, y1]
    snake_blocks.append(snake_head)
    
    # Delete last block of the snake
    if len(snake_blocks) > length_of_snake:
        del snake_blocks[0]
    
    # Check if any of the non-head snake blocks intersect with the head
    for i in snake_blocks[0:-1]:
        if i == snake_head:
            print("u suck")
    
    # Draw the snake, either as michael or normal snake
    draw_snake(snake_blocks)
    #draw_michael(snake_blocks)
    
    # Draw the food either as normal food or as beer
    pygame.draw.rect(dis, green, [food_x, food_y, 10, 10])
    #dis.blit(ol, (food_x, food_y))
    
    # To move the snanke back if it hits the border
    if superchargedX == True:
        x1_change = 10
        superchargedX = False
        print("SuperX")
    
    if superchargedY == True:
        y1_change = 10
        superchargedY = False
        print("SUPERY")
    
    
    et = clock.tick(10)
    elapsed_time += et
    print(elapsed_time)
    
    pygame.display.update()
    
    
    dis.fill(white)

    
    
    
    