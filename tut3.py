import pygame
x=pygame.init()
print(x)

#Creating window
gameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

# Game specific variables
exit_game = False
game_over = False

