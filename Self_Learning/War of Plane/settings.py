import pygame


class Settings(object):
    '''设置常用属性'''
    def __init__(self):
        '''背景图设置'''
        # 加载本地背景图片素材
        self.bgImage = pygame.image.load('img/background.png')
        # 背景图宽
        self.bgImageWidth = self.bgImage.get_rect()[2]
        # 背景图高
        self.bgImageHeight = self.bgImage.get_rect()[3]
        # 游戏开始加载图
        self.start = pygame.image.load('img/start.png')
        # 游戏暂停加载图
        self.pause = pygame.image.load('img/pause.png')
        # 游戏结束加载图
        self.gameover = pygame.image.load('img/gameover.png')
        # 英雄机图片
        self.heroImage = ["img/hero.gif",'img/hero1.png','img/hero2.png']
        # airplane素材
        self.airImage = pygame.image.load("img/enemy0.png")
        # bee的图片
        self.beeImage = pygame.image.load("img/bee.png")
        # 英雄机的子弹
        self.heroBullet = pygame.image.load("img/bullet.png")
        
