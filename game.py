import pygame
import random_list as r
import random

#colors
bgblue = "#82EEFD"
black = "#242526"

class HangMan:

    #printing characters
    def print_char(xB, yB, c, self):
        font_style = pygame.font.Font("EvilEmpire.ttf", 80) 
        mesg = font_style.render(c, True, black)
        self.screenDim.blit(mesg, [xB+100+self.offset, yB+180])
        self.offset = self.offset + 50

    #game loop
    def game_loop(self):
        xB = 0
        yB = 0
        self.screenDim.fill(bgblue) 
        for i in self.arr:
                if(self.guessed_letters.count(i) == 0):
                    HangMan.print_char(xB, yB, '_', self)
                else:
                    HangMan.print_char(xB, yB, i, self)
        while(self.gameover == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover = True
                if event.type == pygame.VIDEORESIZE: 
                    self.screenDim.fill(bgblue)
                    w, h = pygame.display.get_surface().get_size()
                    self.offset = 0 
                    if w!=800:
                        xB = (w-800)/2
                        yB = (h-600)/2
                    else:
                        xB = 0
                        yB = 0  
                    for i in self.arr:
                        if(self.guessed_letters.count(i) == 0):
                            HangMan.print_char(xB, yB, '_', self)
                        else:
                            HangMan.print_char(xB, yB, i, self)
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