import random

import pygame.display

import snehinka
import view

snehinki=[]
debug=False
fps=0


def tasks():
    for snowflake in snehinki:
        snowflake.falling()

def snehinka_paint():
    result = snehinka.Snehinka(random.randint(1, 900), 100,random.randint(1,30)/5)
    snehinki.append(result)

def snehinka_change(pos):
    for snowflake in snehinki:
        snowflake.change(pos)

def move(pos,mouse):
    for snowflake in snehinki:
        snowflake.move(pos,mouse)

def model():
    pass
