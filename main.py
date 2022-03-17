import pygame

WINDOW_HEIGHT = 750
WINDOW_WIDTH = 750
BLOCK_SIZE = 150
GREEN = (50,205,50)

def draw_grid():
    global WINDOW_HEIGHT, WINDOW_WIDTH, BLOCK_SIZE

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(GREEN)

    while True:
        pygame.display.update()

if __name__ == "__main__":
    main()
