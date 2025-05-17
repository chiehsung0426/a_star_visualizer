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

    def reset(self):
        self.color = (255, 255, 255)

    
    def update_neighbors(self, grid):
        self.neighbors = []

        #downward
        if self.row < self.totalrows - 1 and not grid[self.row + 1][self.col].iswall():
            self.neighbors.append(grid[self.row + 1][self.col])
        #upward
        if self.row > 0 and not grid[self.row - 1][self.col].iswall():
            self.neighbors.append(grid[self.row - 1][self.col])
        
        #right
        if self.col < self.totalrows - 1 and not grid[self.row][self.col + 1].iswall():
            self.neighbors.append(grid[self.row][self.col + 1])
        #left
        if self.col > 0 and not grid[self.row][self.col - 1].iswall():
            self.neighbors.append(grid[self.row][self.col - 1])
    
    def iswall(self):
        return self.color == (0, 0, 0)
    
    def get_pos(self):
        return self.row, self.col
    
    def make_open(self):
        self.color = (0, 0, 255)  # Blue

    def make_closed(self):
        self.color = (255, 165, 0)  # Orange

    def make_path(self):
        self.color = (128, 0, 128)  # Purple