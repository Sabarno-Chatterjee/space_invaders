import pygame

# Initialize pygame
pygame.init()

# Game Constants:
HEIGHT = 800
WIDTH = 600
BLACK = (0, 0, 0)

# Setting up the screen
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Screen title
pygame.display.set_caption("Space Invaders")

# Screen icon
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)



# UFO Icon Credit "<a href="https://www.flaticon.com/free-icons/alien" title="alien icons">Alien icons created by Pixel
# Buddha - Flaticon</a>"
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    pygame.display.update()
