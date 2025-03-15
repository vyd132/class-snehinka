import pygame
pygame.init()
snowflake=pygame.image.load('снежинки и капли/snowflake.png')
snowflake=pygame.transform.scale(snowflake,[399/5,346/5])
font=pygame.font.SysFont('arial',50)

class Snehinka():
    def __init__(self,x,y,fall_y):
        self.x=x
        self.y=y
        self.fall_y=fall_y
        self.rect = pygame.rect.Rect([self.x, self.y, 399 / 5, 346 / 5])
        print('work')
    def paint(self,screen:pygame.Surface):
        screen.blit(snowflake,[self.rect.x,self.rect.y+self.fall_y])
        self.fall_y += self.fall_y

    def falling(self):
       pass

    def debug(self,screen:pygame.Surface):
        pygame.draw.rect(screen,[255,255,255],self.rect)
        text=font.render(str(self.fall_y),True,[255,0,0])
        screen.blit(text,self.rect)


