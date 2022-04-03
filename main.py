import pygame
import math
import random

pygame.init()

icon = pygame.image.load("icon.png")
background = pygame.image.load("background.png")
spaceship = pygame.image.load("spaceship.png")
alienship = pygame.image.load("alienship.png")
bullet = pygame.image.load("bullet.png")

spaceshipX = 286
spaceshipY = 520
spaceship_Velocity = 0

alienshipX = []
alienshipY =[]
alienship_Img = []
alienshipY_Change = []
alienshipX_Change = []
number_of_aliens = 7

bulletX = 0
bulletY = 530
bulletX_Change = 0
bulletY_Change = 10
bulletstate = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

gameexit = pygame.font.Font("freesansbold.ttf", 80)

for i in range(number_of_aliens):
    alienship_Img.append(pygame.image.load("alienship.png"))
    alienshipX.append(random.randint(0, 636))
    alienshipY.append(random.randint(50, 100))
    alienshipX_Change.append(4)
    alienshipY_Change.append(40)

def spaceshipImg(x, y):
    window.blit(spaceship, (x, y))

def update():
    pygame.display.update()

def alienshipImg(x, y, i):
    window.blit(alienship_Img[i], (x, y))

def bullet_fire(x, y):
    global bulletstate
    bulletstate = "fire"
    window.blit(bullet, (x+16, y+10))

def Score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    window.blit(score, (x, y))

def game_over():
    game_over = gameexit.render("GAME OVER", True, (255, 255, 255))
    window.blit(game_over, (110, 250))

def iscollision(alienshipX, alienshipY, bulletX, bulletY):
    distance = math.sqrt(math.pow(alienshipX-bulletX, 2) + math.pow(alienshipY-bulletY, 2))
    if distance < 30:
        return True
    else:
        return False

window = pygame.display.set_mode((700,600))
pygame.display.set_caption("Alien Hunt")
pygame.display.set_icon(icon)

gameExit = False
while not gameExit:
    window.fill((0,0,0))
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship_Velocity -= 10
            if event.key == pygame.K_RIGHT:
                spaceship_Velocity += 10
            if event.key == pygame.K_SPACE:
                if bulletstate is "ready":
                    bulletX = spaceshipX
                    bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                spaceship_Velocity = 0
        if event.type == pygame.QUIT:
            gameExit = True

    if spaceshipX <= 0:
        spaceshipX=0
    elif spaceshipX >= 636:
        spaceshipX = 636

    for i in range(number_of_aliens):
        if alienshipY[i] > 450:
            for j in range(number_of_aliens):
                alienshipY[j] = 2000
            game_over()
            break
        alienshipX[i] += alienshipX_Change[i]
        if alienshipX[i] <= 0:
            alienshipX_Change[i] = 4
            alienshipY[i] += alienshipY_Change[i]
        elif alienshipX[i] >= 636:
            alienshipX_Change[i] = -4
            alienshipY[i] += alienshipY_Change[i]
        collision = iscollision(alienshipX[i], alienshipY[i], bulletX, bulletY)
        if collision:
            bulletY = 530
            score_value += 1
            alienshipY[i] = random.randint(50, 100)
            alienshipX[i] = random.randint(0, 636)

        alienshipImg(alienshipX[i], alienshipY[i], i)

    if bulletY <= 0:
        bulletY = 530
        bulletstate = "ready"
    if bulletstate is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_Change

    Score(10, 10)
    spaceshipX += spaceship_Velocity
    spaceshipImg(spaceshipX, spaceshipY)
    update()

pygame.quit()
