import pygame
import random
import math

# Initialize pygame
pygame.init()

# Game Constants:
HEIGHT = 600
WIDTH = 800
BLACK = (0, 0, 0)

# Game variables:
score = 0


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


# UFO Icon Credit "<a href="https://www.flaticon.com/free-icons/alien" title="alien icons">Alien icons created by Pixel
# Buddha - Flaticon</a>"
# Spaceship icon "<a href="https://www.flaticon.com/free-icons/spaceship" title="spaceship icons">Spaceship icons created by Freepik - Flaticon</a>"
# Game Loop
# Invader <a href="https://www.flaticon.com/free-icons/alien" title="alien icons">Alien icons created by smalllikeart - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/bullet" title="bullet icons">Bullet icons created by Darius Dan - Flaticon</a>


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
        # Collision detection:
        collision_check = detect_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision_check < 27:
            bulletY = 480
            bullet_state = "ready"
            score += 1
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


    pygame.display.update()


