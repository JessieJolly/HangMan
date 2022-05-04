import pygame

pygame.init()

screenDim = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Let's play HangMan")
gameover = False
while(gameover == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    pygame.display.update()
pygame.quit()
quit()