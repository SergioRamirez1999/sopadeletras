import pygame
import time
import string
import random

from Cube import Cube
from Grid import Grid
from BoardCreator import create_board, get_words_coords
from Properties import Properties
from ConfigScreen import show_config_screen

show_config_screen()

properties = Properties()
properties._load_properties()

### Parametros Ventana ###
WINDOW_WIDTH = 760
WINDOW_HEIGHT = 820
WINDOW_TITLE = 'Sopa De Letras'
### Parametros adicionales ###
GAME_WORDS = properties.words


def redraw_window(win, grid, time, correct_words):
    win.fill(properties.backgroundColor)
    fnt = pygame.font.SysFont(properties.fontFamily, 40)
    text_time = fnt.render("Tiempo: " + format_time(time), True, (255,0,0))
    win.blit(text_time, (WINDOW_WIDTH - 170, WINDOW_HEIGHT-40))
    grid.draw(win)


def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60
    mat = '{}:{}'.format(str(minute), str(sec))
    return mat


def is_valid_word(grid):
    b_coord = set(grid.board_coord)
    w_coord = get_words_coords()
    #Buscar una forma de retornar la primera ocurrencia / True
    tuple = [(k,v) for k,v in w_coord.items() if set(v)==b_coord]
    if(len(tuple)):
        for t in tuple[0][1]:
            grid.cubes[t[0]][t[1]].found = True
    return len(tuple)


def game_over(win):
    win.fill(properties.COLOR_BLACK)
    fnt = pygame.font.SysFont(properties.fontFamily, properties.fontSize)
    text = fnt.render("Game Over", True, properties.COLOR_WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-50))
    win.blit(text, text_rect)
    pygame.display.update()


pygame.font.init()
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
GAME_BOARD = create_board(GAME_WORDS, properties.orientation)
grid = Grid(GAME_BOARD, WINDOW_WIDTH, WINDOW_HEIGHT-60)
start = time.time()
correct_words = 0


def play_again():
    global GAME_BOARD, grid, start, correct_words
    GAME_BOARD = create_board(GAME_WORDS, properties.orientation)
    grid = Grid(GAME_BOARD, WINDOW_WIDTH, WINDOW_HEIGHT-60)
    start = time.time()
    correct_words = 0


def main_loop():
    global GAME_BOARD, grid, start, correct_words
    key = None
    run = True
    while run:
        play_time = round(time.time() - start)

        for event in pygame.event.get():

            if(event.type == pygame.QUIT):
                run = False
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RETURN):
                    if(is_valid_word(grid)):
                        #Mostrar alguito
                        correct_words += 1
                    if(correct_words == len(GAME_WORDS)):
                        #TODAS LAS PALABRAS ENCONTRADAS
                        game_over(win)
                        waiting = True
                        while(waiting):
                            for event in pygame.event.get():
                                if(event.type == pygame.QUIT):
                                    waiting = False
                                    run = False
                                if(event.type == pygame.KEYDOWN):
                                    if(event.key == pygame.K_RETURN):
                                        waiting = False
                        play_again()
                    grid.board_coord.clear()
                    grid.clear()

            if(event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                clicked = grid.click(pos)
                if clicked:
                    grid.select(clicked[0], clicked[1])
                    key = None

        redraw_window(win, grid, play_time, correct_words)
        pygame.display.update()

main_loop()
pygame.quit()
