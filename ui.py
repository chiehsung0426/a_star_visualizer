# ui.py

import pygame

def draw_instructions(win, width):
    font = pygame.font.SysFont("arial", 18)
    instructions = [
        "L-Click: Set start → end → walls",
        "R-Click: Remove node",
        "ENTER: Start A* search",
        "SPACE: Reset everything",
        "M: Generate random maze"
    ]

    for i, line in enumerate(instructions):
        text = font.render(line, True, (0, 0, 0))
        win.blit(text, (10, width + 10 + i * 20))
