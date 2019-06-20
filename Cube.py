import pygame
import random
import string
from Properties import Properties

properties = Properties()

class Cube:
    def __init__(self, value, row, col, rows, cols, word_type, width, height):
        if(value == ''):
            if(properties.uppercase):
                letter = random.choice(string.ascii_letters).upper()
            else:
                letter = random.choice(string.ascii_letters).lower()
            self.value = letter
        else:
            self.value = value
        self.row = row
        self.col = col
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.word_type = word_type
        self.selected = False
        self.found = False

    def draw(self, win):
        fnt = pygame.font.SysFont(properties.fontFamily, properties.fontSize)

        cell = self.width / self.rows
        x = self.col * cell
        y = self.row * cell

        text = fnt.render(str(self.value), 1, properties.fontColor)
        win.blit(text, (x + (cell/2 - text.get_width()/2), y + (cell/2 - text.get_height()/2)))

        if(self.found and self.word_type == 'noun'):
            pygame.draw.rect(win, properties.colors['noun'], (x,y,cell,cell), 3)
        elif(self.found and self.word_type == 'verb'):
            pygame.draw.rect(win, properties.colors['verb'], (x,y,cell,cell), 3)
        elif(self.found and self.word_type == 'adjective'):
            pygame.draw.rect(win, properties.colors['adjective'], (x,y,cell,cell), 3)
        elif(self.selected):
            pygame.draw.rect(win, (39,216,166), (x,y,cell,cell), 3)

    def __repr__(self):
        return str({'value':self.value, 'row':self.row, 'col':self.col, 'width':self.width, 'height':self.height})
