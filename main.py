import pygame
from node import Node
from algorithm import a_star

WIDTH = 640
ROWS = 20
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Pathfinding Visualizer")



def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        # horizontal line
        pygame.draw.line( win,(200, 200, 200), (0, i * gap), (WIDTH, i * gap))    
        # straight line
        pygame.draw.line( win,(200, 200, 200), (i * gap, 0), (i * gap, WIDTH))

#make each grid includes one node
def make_grid(rows, width):
    grid = []
    gap = width // rows #width for each grid
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid

def draw(win, grid, rows, width):
    win.fill((255, 255, 255))

    for row in grid:
        for node in row:
            node.draw(win) #draw color for each grid
    
    draw_grid(win, rows, width)
    pygame.display.update()


def main():
    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None

    run = True

    for row in grid:
        for node in row:
            node.update_neighbors(grid)

    while run:

        draw(WIN, grid, ROWS, WIDTH)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN: #SPACE to reset
                if event.key == pygame.K_SPACE:
                    start =  None
                    end = None
                    for row in grid:
                        for node in row:
                            node.reset()
                
                elif event.key == pygame.K_RETURN:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    a_star(lambda: draw(WIN, grid, ROWS, WIDTH), grid, start, end)

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row = pos[1] // (WIDTH // ROWS)
                col = pos[0] // (WIDTH // ROWS)

                if 0 <= row < ROWS and 0 <= col < ROWS:
                    node = grid[row][col]

                    if not start:
                        start = node
                        node.make_start()

                    elif not end and node != start:
                        end = node
                        node.make_end()

                    elif node != end and node != start:
                        node.make_wall()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row = pos[1] // (WIDTH // ROWS)
                col = pos[0] // (WIDTH // ROWS)

                if 0 <= row < ROWS and 0 <= col < ROWS:
                    node = grid[row][col]

                    if node == start:
                        start = None
                        node.reset()

                    elif node == end:
                        end = None
                        node.reset()

                    else:
                        node.reset()

    pygame.quit()

main()