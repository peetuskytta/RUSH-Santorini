import pygame
from pygame.locals import *

WINDOW_HEIGHT = 750
WINDOW_WIDTH = 750
BLOCK_SIZE = 150
GREEN = (50,205,50)
WHITE = (250, 250, 250)

def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def main():
    global SCREEN, CLOCK
    print("Enter team name:")
    name = input()
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(GREEN)

    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()

if __name__ == "__main__":
    main()
