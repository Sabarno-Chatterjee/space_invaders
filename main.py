import pygame

pygame.init()

# Game Constants:
HEIGHT = 800
WIDTH = 600
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Space Invaders")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False