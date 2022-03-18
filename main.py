import pygame
from pygame.locals import *

# Sizes in pixels
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 750
BLOCK_SIZE = 150
RES = (950, 750)

# Colors
GREEN = (50,205,50)
WHITE = (250, 250, 250)
DARK = (100, 100, 100)
LIGHTER = (50, 205, 140)



class GameState:
	PLACE_WORKERS = 0
	MID_GAME = 1
	GAMEOVER = 2
	def __init__(self):
		self.phase = GameState.PLACE_WORKERS
		self.number_of_players = 2
		self.turn = 0

class Cell:
	EMPTY = 0
	def __init__(self):
		self.state = Cell.EMPTY

class Grid:
	def __init__(self):
		self.grid = []
		for i in range(0, 5):
			row = []
			for j in range(0, 5):
				row.append(Cell())
			self.grid.append(row)
		print(self.grid)

# Start menu which returns true until clicked START button
def start_menu():

	# menu background
	background = pygame.image.load("santorini_menu.jpg")
	img = pygame.transform.scale(background,(950, 750))

	# Fonts
	smallfont = pygame.font.SysFont('Corbel',35)
	largefont = pygame.font.SysFont('Corbel',70)

	# Texts
	start_button = smallfont.render('Start', True, WHITE)
	q_button = smallfont.render('Quit', True, WHITE)

	# Screen size
	width = SCREEN.get_width()
	height = SCREEN.get_height()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if width/2 <= mouse[0] <= width/2+110 and height/2 <= mouse[1] <= height/2+40:
					pygame.quit()
				if width/2 <= mouse[0] <= width/2+110 and height/2-60 <= mouse[1] <= height/2+40:
					return()
		SCREEN.blit(img, (0, 0))

		mouse = pygame.mouse.get_pos()
		if width/2 <= mouse[0] <= width/2+110 and height/2 <= mouse[1] <= height/2+40:
			pygame.draw.rect(SCREEN, LIGHTER, [width/2, height/2, 110, 40])
		else:
			pygame.draw.rect(SCREEN, DARK, [width/2, height/2, 110, 40])
		SCREEN.blit(q_button, (width/2+25, height/2))

		SCREEN.blit(start_button, (width/2+25, height/2-60))
		pygame.display.update()

# Creating a button to click and start game after names have been given
# CARL!!?!?!? I think it's better to create a uniform button below that can be used all around the menu, right?
def create_button():
	pass

def draw_grid():
	for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
		for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
			rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
			pygame.draw.rect(SCREEN, WHITE, rect, 1)

def main():
	global SCREEN, CLOCK
#	print("Enter team name:")
#	name = input()
	gamestate = GameState()
	grid = Grid()
	pygame.init()
	SCREEN = pygame.display.set_mode(RES, RESIZABLE)
	SCREEN.fill((0, 0, 0))
	#SCREEN.blit(background, (0, 0))
	CLOCK = pygame.time.Clock()
	
	start_menu()
	SCREEN.fill(GREEN)
	while True:
# IDK how to return after clicking START in menu... yet.
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
