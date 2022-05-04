import pygame
import random_list as r
import random

#colors
bgblue = "#82EEFD"
black = "#242526"

class HangMan:

    #printing characters
    def print_char(c, self):
        font_style = pygame.font.Font("EvilEmpire.ttf", 50) 
        mesg = font_style.render(c, True, black)
        self.screenDim.blit(mesg, [100+self.offset, 180])
        self.offset = self.offset + 100

    #game loop
    def game_loop(self):
        self.screenDim.fill(bgblue)
        for i in self.arr:
                if(self.guessed_letters.count(i) == 0):
                    HangMan.print_char('_', self)
                else:
                    HangMan.print_char(i, self)
        while(self.gameover == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover = True
            pygame.display.update()

    def __init__(self) -> None: 
        #initialising the game
        pygame.display.set_caption("Let's play HangMan")
        self.screenDim = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.gameover = False
        #finding a random word
        self.index = random.randrange(len(r.words))
        self.arr = list(r.words[self.index])  
        self.guessed_letters = [] 
        self.offset = 0
        HangMan.game_loop(self)

pygame.init()
HangMan()
pygame.quit()
quit()