import pygame

# Initialize pygame
pygame.init()

# Game Constants:
HEIGHT = 600
WIDTH = 800
BLACK = (0, 0, 0)

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


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


# UFO Icon Credit "<a href="https://www.flaticon.com/free-icons/alien" title="alien icons">Alien icons created by Pixel
# Buddha - Flaticon</a>"
# Spaceship icon "<a href="https://www.flaticon.com/free-icons/spaceship" title="spaceship icons">Spaceship icons created by Freepik - Flaticon</a>"
# Game Loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movements:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.3
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.3

        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
