import pygame
import sys

screen_length  = 800
screen_height  = 600

window = pygame.display.set_mode((screen_length, screen_height))

color = (255, 0, 0)

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

def position(x, y):
    button = pygame.Rect(50, 50)
    button_color = (255, 0, 0)
    pygame.draw.rect(x, y, button_color, button)
position(10, 10)




pygame.display.update()

pygame.quit()
sys.exit()
