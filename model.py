import random

import pygame.display

import snehinka
import view

snehinki=[]
debug=False
fps=0
grabbed=None


def tasks():
    for snowflake in snehinki:
        snowflake.falling()

def snehinka_paint():
    result = snehinka.Snehinka(random.randint(1, 900), 100,random.randint(1,30)/5)
    snehinki.append(result)

def snehinka_change(pos):
    for snowflake in snehinki:
        snowflake.change(pos)

def move(pos):
    for snowflake in snehinki:
        if grabbed==snowflake:
            snowflake.move(pos)

def grab(pos):
    global grabbed
    for snowflake in snehinki:
        if snowflake.rect.collidepoint(pos):
            grabbed=snowflake
            snowflake.fall = False
            return



def release():
    global grabbed
    for snowflake in snehinki:
        if snowflake==grabbed:
            snowflake.fall = True
            grabbed = None

            return

def model():
    pass
