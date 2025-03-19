import pygame,snehinka

import model

pygame.init()
screen=pygame.display.set_mode([1000,1000])
font=pygame.font.SysFont('arial',50)
def view():
    screen.fill([0,0,0])
    text = font.render(str(model.fps), True, [255, 255, 255])
    screen.blit(text,[100,100])

    for snowflake in model.snehinki:
        if model.debug:
            snowflake.debug(screen)
        else:
            snowflake.paint(pygame.display.get_surface())
    pygame.display.flip()