import pygame
import sys
import os
import random
import time
from   pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((1280 , 720))
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
    GROUND_PATH = './graphic/objects/ground.png'


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
        pygame.image.load(BACKGROUND_PATH),
        pygame.image.load(GROUND_PATH)
    )

    ENEMY['cactus'] = (
        pygame.image.load(CACTUS_PATH[0])
    )
    ENEMY['bird'] = (
        pygame.image.load(CACTUS_PATH[1]),
        pygame.image.load(CACTUS_PATH[2])
    )

    return IMAGE,ENEMY

def gethit(hitbox_1 , hitbox_2):
    if ((hitbox_1[0] + hitbox_1[2] >= hitbox_2[0] - hitbox_2[2]) and
        (hitbox_1[0] - hitbox_1[2] <= hitbox_2[0] + hitbox_2[2]) and
        (hitbox_1[1] + hitbox_1[3] >= hitbox_2[1] - hitbox_2[3]) and
        (hitbox_1[1] - hitbox_1[3] <= hitbox_2[1] + hitbox_2[3])):
        return True
    return False

IMAGES , ENEMYS = load()

BACKGROUND_w = IMAGES['background'][0].get_width()
BACKGROUND_h = IMAGES['background'][0].get_height()
bgx = 0
bgx2 = BACKGROUND_w
class Player(object):
    def __init__(self):
        self.width = IMAGES['player'][0].get_width()
        self.hight = IMAGES['player'][0].get_height()
        self.x = int(BACKGROUND_w*0.05)
        self.y = int((650 - self.hight))
        self.isjump = False
        self.walkCount = 0
        self.jumpCount = 3.5
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
        self.hitbox_1 = (self.x+130 , self.y+120 , 50 , 70)
        self.hitbox_2 = (self.x+120 , self.y+20 , 120 , 60)
        pygame.draw.rect(win , (255,0,0) , self.hitbox_1 , 2)
        pygame.draw.rect(win , (255,0,0) , self.hitbox_2 , 2)

class cactus(object):
    def __init__(self):
        
        self.vel = 30
        self.width = ENEMYS['cactus'].get_width()
        self.hight = ENEMYS['cactus'].get_height()
        self.x =  int(BACKGROUND_w + (random.randint(-200,1000)))
        self.y = int((650 - self.hight) )
    def draw(self):   
        win.blit(ENEMYS['cactus'], (self.x,self.y))
        self.rect = (self.x+20 , self.y+25 , 50 , 50)
        pygame.draw.rect(win , (255,0,0) , self.rect , 2)

class bird(object):
    def __init__(self):
        self.x = int(BACKGROUND_w)
        self.y = int(BACKGROUND_h * 0.6 + (random.choice([-100,100])))
        self.vel = 25
        self.width = ENEMYS['bird'][0].get_width()
        self.hight = ENEMYS['bird'][0].get_height()
        self.birdcount=0
    def draw(self):
        if self.birdcount >= 1:
            self.birdcount = 0
        win.blit(ENEMYS['bird'][self.birdcount], (self.x,self.y))
        self.birdcount += 1
        self.hitbox = (self.x , self.y , 100 , 60)
        pygame.draw.rect(win , (255,0,0) , self.hitbox , 2)


class Game_State:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont ('comicsans' , 50 , True)
        self.girl = Player()
        self.cactus_1 = cactus()
        self.cactus_2 = cactus()
        self.cactus_list = [self.cactus_1, self.cactus_2]
        self.jumpCount=0
        self.groundx = 0
        self.groundx2 =650
        self.bird_list = []
    def redrawGame(self):
        win.blit(IMAGES['background'][0], (bgx,0))
        win.blit(IMAGES['background'][0], (bgx2,0))
        win.blit(IMAGES['background'][1], (self.groundx,650))
        win.blit(IMAGES['background'][1], (self.groundx2,650))
        self.girl.draw()
        self.cactus_list[0].draw()
        self.text = self.font.render('score: '+ str(self.score), 1 ,(0,0,0))
        win.blit(self.text, (800, 20))
        for index in range(len(self.bird_list)):
            self.bird_list[index-1].draw()
    def frame_step(self):        
        while True:
            global bgx
            global bgx2

            self.redrawGame()
            pygame.display.update()
            bgx -= 2
            if bgx <= BACKGROUND_w * -1 :
                bgx = BACKGROUND_w
            bgx2 -= 2
            if bgx2 <= BACKGROUND_w * -1 :
                bgx2 = BACKGROUND_w
            self.groundx -= 40
            if self.groundx <= BACKGROUND_w * -1 :
                self.groundx = BACKGROUND_w
            self.groundx2 -= 40
            if self.groundx2 <= BACKGROUND_w * -1 :
                self.groundx2 = BACKGROUND_w
            
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
                if self.girl.jumpCount >= -3.5:
                    self.neg = 10
                    if self.girl.jumpCount < 0:
                        self.neg = -10
                    self.girl.y -= (self.girl.jumpCount **2 ) * self.neg 
                    self.girl.jumpCount -= 0.7
                else:
                    self.girl.isjump = False
                    self.girl.jumpCount = 3.5

            if self.girl.isslide:
                if self.girl.slidecount >= 23:
                    self.girl.isslide = False
                    self.girl.slidecount = 18
            self.col = gethit(self.girl.hitbox_1 , self.cactus_list[0].rect )
            if self.col == True:
                self.__init__()
            else:
                self.score +=1
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

          
            clock.tick(20)



game = Game_State()
game.frame_step()
