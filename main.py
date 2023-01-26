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
playerImg = pygame.image.load()



# UFO Icon Credit "<a href="https://www.flaticon.com/free-icons/alien" title="alien icons">Alien icons created by Pixel
# Buddha - Flaticon</a>"
# Spaceship icon "<a href="https://www.flaticon.com/free-icons/spaceship" title="spaceship icons">Spaceship icons created by Freepik - Flaticon</a>"
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    pygame.display.update()
