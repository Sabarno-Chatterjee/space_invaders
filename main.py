import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Game Constants:
HEIGHT = 600
WIDTH = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Score:
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over:
game_over_X = 300
game_over_Y = 250

# Setting up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Screen title
pygame.display.set_caption("Space Invaders")

# Screen icon
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = 4
enemyY_change = 40
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"
# Background
backgroundIMG = pygame.image.load("background.png")


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def detect_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    return distance


def show_score(x, y):
    score = font.render(f"Score:{score_value}", True, WHITE)
    screen.blit(score, (x, y))


def game_over(x, y):
    game_over = font.render("GAME OVER!", True, WHITE)
    screen.blit(game_over, (x, y))


running = True
while running:
    screen.fill(BLACK)
    screen.blit(backgroundIMG, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movements:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 7
            if event.key == pygame.K_RIGHT:
                playerX_change += 7
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX += playerX_change

    # Enemy movements:
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change
        if enemyX[i] <= 0:
            enemyX_change = 2
            enemyY[i] += enemyY_change
        elif enemyX[i] > 736:
            enemyX_change = - 2
            enemyY[i] += enemyY_change

        if enemyY[i] > 440:
            # running = False
            game_over(game_over_X, game_over_Y)
            bullet_state = "empty"
            restart = font.render("Space to restart", True, WHITE)
            screen.blit(restart, (285, 400))
            break

        # Collision detection:
        collision_check = detect_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision_check < 27:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement:
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    # Player movements:
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
