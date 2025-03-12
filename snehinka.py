import pygame
snowflake=pygame.image.load('снежинки и капли/snowflake.png')
snowflake=pygame.transform.scale(snowflake,[399/5,346/5])

class Snehinka():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rect = pygame.rect.Rect([self.x, self.y, 399 / 5, 346 / 5])
        print('work')
    def paint(self,screen:pygame.Surface):
        screen.blit(snowflake,[self.rect.x,self.rect.y])
    def falling(self):
        self.rect.y+=2
