import pygame
import random_list as r
import random
import list_letters as ll

#colors
bgblue = "#82EEFD"
black = "#242526"
white = "#FFFFFF"

class HangMan:
    #printing the guessed letters
    def print_guessed_char(xB, yB, self):
        font_style = pygame.font.Font("EvilEmpire.ttf", 30)
        mesg = font_style.render("Guessed Letters: ", True, black)
        self.screenDim.blit(mesg, [xB+100, yB+300])
        gx_offset = 0
        gy_offset = 30
        _count = 0
        for letter in self.guessed_letters:
            if(_count >0 and _count%10 == 0):
                gx_offset = 0
                gy_offset = gy_offset + 30
            let = font_style.render(letter, True, black)
            self.screenDim.blit(let, [xB+100+gx_offset, yB+300+gy_offset])
            gx_offset = gx_offset + 30
            _count = _count+1
    #printing characters
    def print_char(xB, yB, c, self):
        font_style = pygame.font.Font("EvilEmpire.ttf", 60) 
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
        pygame.draw.rect(self.screenDim, white, pygame.Rect(xB+80, yB+130, 630, 130))
        pygame.draw.rect(self.screenDim, black, pygame.Rect(xB+580, yB+350, 36, 36), 3, 35)
        pygame.draw.line(self.screenDim, black, (xB+598, yB+350), (xB+598, yB+330), 3)
        pygame.draw.line(self.screenDim, black, (xB+598, yB+330), (xB+650, yB+330), 3)
        pygame.draw.line(self.screenDim, black, (xB+650, yB+330), (xB+650, yB+510), 3)
        pygame.draw.line(self.screenDim, black, (xB+665, yB+510), (xB+600, yB+510), 3)
        pygame.draw.line(self.screenDim, black, (xB+598, yB+386), (xB+598, yB+440), 3)
        #limbs
        pygame.draw.line(self.screenDim, black, (xB+598, yB+440), (xB+578, yB+460), 4)
        pygame.draw.line(self.screenDim, black, (xB+598, yB+440), (xB+618, yB+460), 4)
        pygame.draw.line(self.screenDim, black, (xB+598, yB+413), (xB+618, yB+413), 3)
        pygame.draw.line(self.screenDim, black, (xB+598, yB+413), (xB+578, yB+413), 3)
        HangMan.call_print(xB, yB, self)
        HangMan.print_guessed_char(xB, yB, self)
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
                    pygame.draw.rect(self.screenDim, white, pygame.Rect(xB+80, yB+130, 630, 130))
                    HangMan.call_print(xB, yB, self)
                    HangMan.print_guessed_char(xB, yB, self)
                if event.type == pygame.KEYDOWN: 
                    if event.key in ll.letters and chr(event.key) not in self.guessed_letters:
                        self.guessed_letters.append(chr(event.key))
                        self.screenDim.fill(bgblue)
                        pygame.draw.rect(self.screenDim, white, pygame.Rect(xB+80, yB+130, 630, 130))
                        self.offset = 0
                        HangMan.call_print(xB, yB, self)
                        HangMan.print_guessed_char(xB, yB, self)
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