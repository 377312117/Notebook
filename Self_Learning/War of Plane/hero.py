from flyingObject import FlyingObject
from bullet import Bullet
import pygame

class Hero(FlyingObject):
    '''此类为英雄机'''
    # 标志位
    index = 2
    def __init__(self,screen,image):
        self.screen = screen
        # 英雄级图片数组，为Surface实例
        self.images = images
        image = pygame.image.load(image[0])
        x = screen.get_rect().centerx
        y = screen.get_rect().bottom
        super().__init__(screen,x,y,image)
        # 生命值为3
        self.life = 3  
        # 初始火力值为0
        self.doubleFire = 0

    def isDoubleFire(self):
        '''获取双倍火力'''
        return self.doubleFire

    def setDoubleFire(self):
        self.doubleFire = 40

    def addDoubleFire(self):
        


