import pygame
import main

class movement:
    def basic_movement():
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            main.player.move_ip(-1,0)
        elif key[pygame.K_d] == True:
            main.player.move_ip(1,0)
        elif key[pygame.K_w] == True:
            main.player.move_ip(0,-1)
        elif key[pygame.K_s] == True:
            main.player.move_ip(0,1)