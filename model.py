import random

import pygame.display

import snehinka
import view

snehinki=[]
debug=False
fps=0
grabbed=None
snowflake=snehinka.Snehinka(750, 50,5)

water=snehinka.Snehinka(850, 50,5)
water.change_water()




def snowflake_buy(pos):
    global grabbed
    if snowflake.rect.collidepoint(pos):
        result = snehinka.Snehinka(750, 50, random.randint(1, 30) / 5)
        # grabbed=result
        snehinki.append(result)

def water_buy(pos):
    global grabbed
    if water.rect.collidepoint(pos):
        result = snehinka.Snehinka(850, 50, random.randint(1, 30) / 5)
        # grabbed=result
        result.change_water()
        snehinki.append(result)

def tasks():
    for snowflake in snehinki:
        snowflake.falling()

def snehinka_paint():
    result = snehinka.Snehinka(random.randint(1, 900), 100,random.randint(1,30)/5)
    snehinki.append(result)

def snehinka_change(pos):
    for snowflake in snehinki:
        if snowflake.rect.collidepoint(pos):
            snowflake.change_water()

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
            snowflake.color_change = True
            snowflake.color_timer_on()
            return



def release():
    global grabbed
    for snowflake in snehinki:
        if snowflake==grabbed:
            snowflake.fall = True
            grabbed = None
            snowflake.color_timer_off()
            return

def color_change():
    if grabbed==None:
        return
    grabbed.change_color()


def model():
    pass
