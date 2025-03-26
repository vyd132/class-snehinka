import pygame
pygame.init()
snowflake=pygame.image.load('снежинки и капли/snowflake.png')
snowflake=pygame.transform.scale(snowflake,[399/5,346/5])

water=pygame.image.load('снежинки и капли/water_drop.png')
water=pygame.transform.scale(water,[526/10,959/10])

snowflake_active=pygame.image.load('снежинки и капли/snowflake2.png')
snowflake_active=pygame.transform.scale(snowflake_active,[399/5,346/5])

font=pygame.font.SysFont('arial',50)

class Snehinka():
    def __init__(self,x,y,fall_y):
        self.fall_y=fall_y
        self.rect = pygame.rect.Rect([x, y, snowflake.get_height(), snowflake.get_height()])
        self.alt_y=y
        self.current_image=snowflake
        self.fall=True
        self.color_change=False
        self.timer=None
    def paint(self,screen:pygame.Surface):
        screen.blit(self.current_image,[self.rect.x,self.rect.y])


    def falling(self):
        if self.fall!=True:
            return
        self.alt_y+=self.fall_y
        self.rect.y=self.alt_y

    def debug(self,screen:pygame.Surface):
        pygame.draw.rect(screen,[255,255,255],self.rect)
        text=font.render(str(self.fall_y),True,[255,0,0])
        screen.blit(text,self.rect)

    def change_water(self):
        self.current_image=water
        self.rect.width=water.get_width()
        self.rect.height =water.get_height()
        self.fall_y=10

    def move(self,pos):
        self.rect.centerx=pos[0]
        self.rect.centery=pos[1]
        self.alt_y= self.rect.y

    def change_color(self):
        if self.current_image==snowflake:
            self.current_image=snowflake_active
        else:
            self.current_image = snowflake

    def color_timer_on(self):
        self.timer=pygame.event.custom_type()
        pygame.time.set_timer(self.timer,int(1/self.fall_y*1000))


    def color_timer_off(self):
        self.timer=pygame.time.set_timer(self.timer,0)
        self.current_image = snowflake



    def controller(self,events):
        for event in events:
            if self.timer!=None and event.type==self.timer:
                self.change_color()
