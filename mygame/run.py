import pygame
import sys
import os
import random
import time
from   pygame.locals import *

pygame.init()
win = pygame.display.set_mode((1280 , 960))
pygame.display.set_caption('runrunrun')

def load():
    PLAYER_PATH = (
        './graphic/Run (1)(已去底).png',
        './graphic/Run (2)(已去底).png',
        './graphic/Run (3)(已去底).png',
        './graphic/Run (4)(已去底).png',
        './graphic/Run (5)(已去底).png',
        './graphic/Run (6)(已去底).png',
        './graphic/Run (7)(已去底).png',
        './graphic/Run (8)(已去底).png',
        './graphic/Jump (1)(已去底).png',
        './graphic/Jump (2)(已去底).png',
        './graphic/Jump (3)(已去底).png',
        './graphic/Jump (4)(已去底).png',
        './graphic/Jump (5)(已去底).png',
        './graphic/Jump (6)(已去底).png',
        './graphic/Jump (7)(已去底).png',
        './graphic/Jump (8)(已去底).png',
        './graphic/Jump (9)(已去底).png',
        './graphic/Jump (10)(已去底).png',
        './graphic/Slide (1)(已去底).png',
        './graphic/Slide (2)(已去底).png',
        './graphic/Slide (3)(已去底).png',
        './graphic/Slide (4)(已去底).png',
        './graphic/Slide (5)(已去底).png'
    )

    CACTUS_PATH = ('./graphic/Objects/Cactus (1).png',
                    './graphic/Objects/1(已去底).png',
                    './graphic/Objects/2(已去底).png'
                )

    BACKGROUND_PATH = './graphic/BG.png'


    IMAGE = {}
    ENEMY = {}


    IMAGE['player'] = (
        pygame.image.load(PLAYER_PATH[0]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[1]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[2]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[3]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[4]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[5]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[6]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[7]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[8]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[9]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[10]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[11]).convert_alpha(),    
        pygame.image.load(PLAYER_PATH[12]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[13]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[14]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[15]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[16]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[17]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[18]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[19]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[20]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[21]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[22]).convert_alpha()
    )

    IMAGE['background'] = (
        pygame.image.load(BACKGROUND_PATH)
    )

    ENEMY['cactus'] = (
        pygame.image.load(CACTUS_PATH[0])
    )
    ENEMY['bird'] = (
        pygame.image.load(CACTUS_PATH[1]),
        pygame.image.load(CACTUS_PATH[2])
    )

    return IMAGE,ENEMY

IMAGES , ENEMYS = load()

BACKGROUND_w = IMAGES['background'].get_width()
BACKGROUND_h = IMAGES['background'].get_height()
class Player(object):
    def __init__(self):
        self.width = IMAGES['player'][0].get_width()
        self.hight = IMAGES['player'][0].get_height()
        self.x = int(BACKGROUND_w*0.05)
        self.y = int(BACKGROUND_h * 0.6)
        self.isjump = False
        self.walkCount = 0
        self.jumpCount = 5
        self.jcount = 8
        self.slidecount =18
        self.isslide = False
    def draw(self):
        if not (self.isjump or self.isslide):
            if self.walkCount >= 8:
                self.walkCount = 0
            win.blit(IMAGES['player'][self.walkCount], (self.x,self.y))
            self.walkCount += 1
        if self.isjump and not(self.isslide):
            if self.jcount>=18:
                self.jcount = 8
            win.blit(IMAGES['player'][self.jcount], (self.x,self.y))
            self.jcount += 1
        if self.isslide :
            if self.slidecount>=23:
                self.slidecount = 18
            win.blit(IMAGES['player'][self.slidecount], (self.x , self.y))
            self.slidecount += 1

class cactus(object):
    def __init__(self):
        self.x =  int(BACKGROUND_w + (random.randint(-200,1000)))
        self.y = int(BACKGROUND_h * 0.7) 
        self.vel = 50
        self.width = ENEMYS['cactus'].get_width()
        self.hight = ENEMYS['cactus'].get_height()
    def draw(self):   
        win.blit(ENEMYS['cactus'], (self.x,self.y))

class bird(object):
    def __init__(self):
        self.x = int(BACKGROUND_w)
        self.y = int(BACKGROUND_h * 0.6 + (random.randint(-300,100)))
        self.vel = 50
        self.width = ENEMYS['bird'][0].get_width()
        self.hight = ENEMYS['bird'][0].get_height()
        self.birdcount=0
    def draw(self):
        if self.birdcount >= 1:
            self.birdcount = 0
        win.blit(ENEMYS['bird'][self.birdcount], (self.x,self.y))
        self.birdcount += 1

class Game_State:
    def __init__(self):
        self.score = 0
        self.girl = Player()
        self.cactus_1 = cactus()
        self.cactus_2 = cactus()
        self.cactus_list = [self.cactus_1, self.cactus_2]
        self.jumpCount=0
        self.bird_list = []
    def redrawGame(self):
        win.blit(IMAGES['background'], (0,0))
        self.girl.draw()
        self.cactus_list[0].draw()
        for index in range(len(self.bird_list)):
            self.bird_list[index-1].draw()
    def frame_step(self):        
        while True:
            pygame.time.delay(30)
            self.redrawGame()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()
            if not(self.girl.isjump):
                if keys[pygame.K_SPACE]:
                    self.girl.isjump = True
                    self.girl.walkCount = 0
            if not(self.girl.isslide):
                if keys[pygame.K_DOWN]:
                    self.girl.isslide = True
                    self.girl.slidecount = 18
            
            if self.girl.isjump :
                if self.girl.jumpCount >= -5:
                    self.neg = 5
                    if self.girl.jumpCount < 0:
                        self.neg = -5
                    self.girl.y -= (self.girl.jumpCount ** 2) * self.neg
                    self.girl.jumpCount -= 1
                else:
                    self.girl.isjump = False
                    self.girl.jumpCount = 5

            if self.girl.isslide:
                if self.girl.slidecount >= 23:
                    self.girl.isslide = False
                    self.girl.slidecount = 18

            if self.cactus_list[0].x <= 0:
                self.cactus_list.pop(0)
                self.new_cactus = cactus()
                self.cactus_list.append(self.new_cactus)
            if self.cactus_list[0].x >= 0:
                self.cactus_list[0].x -= self.cactus_list[0].vel

            if random.randint(0,200) == 1:
                self.new_bird = bird()
                self.bird_list.append(self.new_bird)
            if len(self.bird_list) != 0:
                for index in range(len(self.bird_list)):
                    self.bird_list[index-1].x -= self.bird_list[index-1].vel
                    if self.bird_list[0].x <= -self.bird_list[0].width:
                        self.bird_list.pop(0)




game = Game_State()
game.frame_step()
