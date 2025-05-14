import pygame

class Node:
    def __init__(self, row, col, width, totalrows):
        self.row = row
        self.col = col
        self.width = width
        self.x = width * col
        self.y = width * row
        self.totalrows = totalrows
        self.color = (255, 255, 255)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def make_start(self):
        self.color = (0, 255, 0)
    def make_end(self):
        self.color = (255, 0, 0)
    def make_wall(self):
        self.color = (0, 0, 0)