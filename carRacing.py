import pygame
from sys import exit
from random import choice

pygame.init()
width = 650
height = 700
displayScreen = pygame.display.set_mode([width, height])

class Road:
    def __init__(self):
        self.image = pygame.image.load("images/Road.png").convert_alpha()
        self.move = True
        self.y = 0
    
    def showRoad(self):
        displayScreen.blit(self.image, [0, self.y-700])
        displayScreen.blit(self.image, [0, self.y])
        displayScreen.blit(self.image, [0, self.y+700])
    
    def moveRoad(self):
        if self.move:
            if self.y == 700:
                self.y = -700
            self.y += 10

class Car:
    def __init__(self):
        self.carRed = pygame.image.load("images/Car1.png").convert_alpha()
        self.carPink = pygame.image.load("images/Car2.png").convert_alpha()
        self.carWhite = pygame.image.load("images/Car3.png").convert_alpha()
        self.carSkyBlue = pygame.image.load("images/Car4.png").convert_alpha()
        self.carLightGreen = pygame.image.load("images/Car5.png").convert_alpha()
        self.carPurple = pygame.image.load("images/Car6.png").convert_alpha()
        self.carGreen = pygame.image.load("images/Car7.png").convert_alpha()
        self.variables()
        self.enemyVariables()

    def variables(self):
        self.playerCarImg = self.carSkyBlue
        self.playerRect = self.playerCarImg.get_rect(topleft = (350, 540))
    
    def enemyVariables(self):
        self.enemyCarImg1 = self.getCar()[0]
        self.enemyCarImg2 = self.getCar()[0]
        self.enemyCarRect1 = self.enemyCarImg1.get_rect(topleft = (85, -150))
        self.enemyCarRect2 = self.enemyCarImg2.get_rect(topleft = (220, 350))
    
    def enemyCar(self):
        displayScreen.blit(self.enemyCarImg1, self.enemyCarRect1)
        displayScreen.blit(self.enemyCarImg2, self.enemyCarRect2)
        self.moveEnemyCar()

    def moveEnemyCar(self):
        if self.enemyCarRect1.y > 700:
            self.enemyCarImg1 = self.getCar()[0]
            self.enemyCarRect1.x = self.getCar()[1]
            self.enemyCarRect1.y = -150
        self.enemyCarRect1.y += 5
        if self.enemyCarRect2.y > 700:
            self.enemyCarImg2 = self.getCar()[0]
            self.enemyCarRect2.x = self.getCar()[1]
            self.enemyCarRect2.y = -150
        self.enemyCarRect2.y += 5
    def playerCar(self):
        displayScreen.blit(self.playerCarImg, self.playerRect)
    
    def getCar(self):
        x = choice([85, 220, 350, 490])
        car = choice([self.carRed, self.carPink, self.carWhite, self.carSkyBlue, self.carLightGreen, self.carPurple, self.carGreen])
        return car, x

class Main:
    def __init__(self) -> None:
        self.move = False
        self.gameRun = False
        self.start = True
        self.showscr = 0
        self.score = 0

    def startScreen(self):
        road.showRoad()
        font = pygame.font.SysFont("Cascadia Code", 70, True, True)
        text01 = font.render("START", True, "white", "red")
        text02 = font.render("START", True, "white", "black")
        text11 = font.render("QUIT", True, "red", "white")
        text12 = font.render("QUIT", True, "black", "white")
        text_rect = text01.get_rect(topleft = [100, 400])
        text2_rect = text11.get_rect(topleft = [400, 400])
        if text_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(3)[0]:
                self.start = False
                self.gameRun = True
                self.move = True
            displayScreen.blit(text02, text_rect)
        elif text2_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(3)[0]:
                pygame.quit()
                exit()
            displayScreen.blit(text12, text2_rect)
        else:
            displayScreen.blit(text01, text_rect)
            displayScreen.blit(text11, text2_rect)

    def gameOverScreen(self):
        road.showRoad()
        font = pygame.font.SysFont("Cascadia Code", 70, True, True)
        font2 = pygame.font.SysFont("Cascadia Code", 130, True, True)
        font2.underline = True
        text = font2.render("GAMEOVER", True, (0, 255, 255))
        text30 = font.render("Score :- "+str(self.showscr), True, (0, 255, 255))
        text01 = font.render("RESTART", True, "white", "red")
        text02 = font.render("RESTART", True, "white", "black")
        text11 = font.render("QUIT", True, "red", "white")
        text12 = font.render("QUIT", True, "black", "white")
        text_rect = text01.get_rect(topleft = [50, 500])
        text2_rect = text11.get_rect(topleft = [400, 500])
        if text_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(3)[0]:
                self.gameRun = True
                self.move = True
            displayScreen.blit(text02, text_rect)
        elif text2_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(3)[0]:
                pygame.quit()
                exit()
            displayScreen.blit(text12, text2_rect)
        else:
            displayScreen.blit(text01, text_rect)
            displayScreen.blit(text11, text2_rect)
        displayScreen.blit(text, [30, 100])
        displayScreen.blit(text30, [200, 300])
    
    def gameOver(self):
        if car.playerRect.collidelist([car.enemyCarRect1, car.enemyCarRect2]) != -1:
            car.playerRect.topleft = (350, 540)
            car.enemyCarRect1.topleft = (85, -150)
            car.enemyCarRect2.topleft = (220, 200)
            self.gameRun = False
            self.move = False
            self.showscr = self.score
            self.score = 0
    
    def showScore(self):
        font = pygame.font.SysFont("Cascadia Code", 50, False, True)
        font.underline = True
        score = font.render("Score "+str(self.score), True, "red")
        displayScreen.blit(score, [(650-score.get_width())/2, 100])

    def update(self):
        if self.start:
            self.startScreen()
        elif self.gameRun:
            road.showRoad()
            road.moveRoad()
            car.playerCar()
            car.enemyCar()
            self.gameOver()
            self.showScore()
        else:
            self.gameOverScreen()

clock = pygame.time.Clock()
fps = 60

road = Road()
car = Car()
game = Main()

comingCar = pygame.USEREVENT
pygame.time.set_timer(comingCar, 500)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == comingCar:
            if game.gameRun:
                game.score += 1
        if event.type == pygame.KEYDOWN:
            if game.move:
                if event.key == pygame.K_LEFT:
                    if car.playerRect.left > 40:
                        car.playerRect.centerx -= 40
                if event.key == pygame.K_RIGHT:
                    if car.playerRect.right < 600:
                        car.playerRect.centerx += 40
                if event.key == pygame.K_UP:
                    if car.playerRect.top > 20:
                        car.playerRect.centery -= 40
                if event.key == pygame.K_DOWN:
                    if car.playerRect.bottom < 690:
                        car.playerRect.centery += 40
    game.update()
    pygame.display.update()
    clock.tick(fps)