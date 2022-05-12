import pygame
import random_list as r
import random
import list_letters as ll

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

    #function to print all letters
    def call_print(xB, yB, self):
        for i in self.arr:
                if(self.guessed_letters.count(i) == 0):
                    HangMan.print_char(xB, yB, '_', self)
                else:
                    HangMan.print_char(xB, yB, i, self)
    #game loop
    def game_loop(self):
        xB = 0
        yB = 0
        self.screenDim.fill(bgblue) 
        HangMan.call_print(xB, yB, self)
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
                    HangMan.call_print(xB, yB, self)
                if event.type == pygame.KEYDOWN:
                    if event.key in ll.letters:
                        self.guessed_letters.append(chr(event.key))
                        self.screenDim.fill(bgblue)
                        self.offset = 0
                        HangMan.call_print(xB, yB, self)
#test here
                        print(self.guessed_letters)
            pygame.display.update()

    def __init__(self) -> None: 
        #initialising the game
        pygame.display.set_caption("Let's play HangMan")
        self.screenDim = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.gameover = False
        #finding a random word
        self.index = random.randrange(len(r.words))
        self.arr = list(r.words[self.index]) 
#test here
        print(self.arr)
        self.guessed_letters = [] 
        self.offset = 0 
        HangMan.game_loop(self)

pygame.init()
HangMan()
pygame.quit()
quit()