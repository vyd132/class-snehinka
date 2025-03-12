import pygame,snehinka

import model

pygame.init()
screen=pygame.display.set_mode([1000,1000])

def view():
    screen.fill([0,0,0])
    model.result.paint(screen)
    pygame.display.flip()