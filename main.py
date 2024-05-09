import pygame
import functions_movement

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((300,250,50,50))

game_run = True
while game_run:
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255,0,0), player)

    functions_movement.movement.basic_movement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
    
    pygame.display.update()

pygame.quit()