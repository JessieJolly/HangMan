import pygame
import random as r

pygame.init()

#colors
bgblue = "#82EEFD"

screenDim = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Let's play HangMan")
gameover = False
print(r.words[0])
while(gameover == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    screenDim.fill(bgblue)
    pygame.display.update()
pygame.quit()
quit()