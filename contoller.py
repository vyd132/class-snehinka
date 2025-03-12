import pygame

import model


pygame.init()

type_model=pygame.event.custom_type()
pygame.time.set_timer(type_model,60)
spawn_timer=pygame.event.custom_type()
pygame.time.set_timer(spawn_timer,2000)
def contoller():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type==type_model:
            model.tasks()
        if event.type==spawn_timer:
            model.result.paint()