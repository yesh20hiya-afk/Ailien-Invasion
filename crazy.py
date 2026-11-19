import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y =10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('background.png')
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
player_img = pygame.image.load('player.png')
PlayerX = PLAYER_START_X
PlayerY = PLAYER_START_Y
PlayerX_change = 0

Enemy_img = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    Enemy_img.append(pygame.image.load('enemy.png'))
    EnemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    EnemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    EnemyX_change.append(ENEMY_SPEED_X)
    EnemyY_change.append(ENEMY_SPEED_Y)

bullet_img = pygame.image.load('bullet.png')
BulletX = 0
BulletY = PLAYER_START_Y
BulletX_change = 0
BulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    screen.blit(player_img, (x, y))
def enemy(x, y, i):
    screen.blit(Enemy_img[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance < COLLISION_DISTANCE

running = True 
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        
    




