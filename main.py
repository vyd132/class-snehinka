import time

import pygame.time

import contoller,view,model

clock=pygame.time.Clock()

while True:
    clock.tick(60)
    model.fps=clock.get_fps()
    contoller.contoller()
    model.model()
    view.view()
