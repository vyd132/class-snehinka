import pygame

import model,snehinka


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
            model.snehinka_paint()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
            model.debug=not model.debug
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==pygame.BUTTON_LEFT:
            model.snehinka_change(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT:
            model.grab(event.pos)
        if event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_RIGHT:
            model.release()
        if event.type==pygame.MOUSEMOTION:
            model.move(event.pos)
            pygame.display.set_caption(str(event.pos))
