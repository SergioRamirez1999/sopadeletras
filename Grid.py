import pygame
from Cube import Cube
from Properties import Properties

properties = Properties()

class Grid:
    def __init__(self, board, width, height):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.cubes = [[Cube(self.board[i][j][0], i, j, self.rows, self.cols, self.board[i][j][1], width, height) for j in range(self.cols)] for i in range(self.rows)]
        self.width = width
        self.height = height
        self.selected = None
        self.board_coord = []


    def select(self, row, col):
        if(self.cubes[row][col].selected and not self.cubes[row][col].found):
            self.cubes[row][col].selected = False
            coords = (self.cubes[row][col].row, self.cubes[row][col].col)
            if(coords in self.board_coord):
                self.board_coord.remove(coords)
        else:
            self.cubes[row][col].selected = True
        self.selected = (row, col)


    def click(self, pos):
        if(pos[0] < self.width and pos[1] < self.height):
            cell = self.width / self.rows
            x = pos[0] // cell
            y = pos[1] // cell
            coords = (int(y), int(x))
            if(properties.orientation == 'vertical'):
                if(len(self.board_coord)>=1):
                    if(self.board_coord[0][1]!=int(x)):
                        return None
                    if(not coords in self.board_coord and not self.cubes[coords[0]][coords[1]].found):
                        self.board_coord.append(coords)
                else:
                    self.board_coord.append(coords)
            else:
                if(len(self.board_coord)>=1):
                    if(self.board_coord[0][0]!=int(y)):
                        return None
                    if(not coords in self.board_coord and not self.cubes[coords[0]][coords[1]].found):
                        self.board_coord.append(coords)
                else:
                    self.board_coord.append(coords)
            return coords
        else:
            return None


    def clear(self):
        for i in range(self.rows):
            for h in range(self.cols):
                self.cubes[i][h].selected = False


    def draw(self, win):
        cell = self.width / self.rows
        for i in range(self.rows+1):
            pygame.draw.line(win, properties.linesColor, (0, i*cell), (self.width, i*cell), 1)
            pygame.draw.line(win, properties.linesColor, (i*cell, 0), (i*cell, self.height), 1)
        for i in range(self.rows):
            for h in range(self.cols):
                self.cubes[i][h].draw(win)
