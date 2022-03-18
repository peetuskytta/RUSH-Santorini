import pygame
from pygame.locals import *

# Sizes in pixels
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 950
BLOCK_SIZE = 150
RES = (950, 750)

# Colors
GREEN = (50,205,50)
RED = (205,50,50)
BLUE = (50,50,205)
WHITE = (250, 250, 250)
DARK = (100, 100, 100)
LIGHTER = (50, 205, 140)

class Player:
	def __init__(self):
		self.name = "Noname"

class GameState:
	PLACE_WORKERS = 0
	MID_GAME = 1
	GAMEOVER = 2
	def __init__(self):
		self.phase = GameState.PLACE_WORKERS
		self.number_of_players = 2
		self.turn = 0
		self.current_player = 1
		#self.players == [Player(), Player()]

class Cell:
	def __init__(self):
		self.height = 0
		self.occupied_by = 0

class Grid:
	def __init__(self):
		self.grid = []
		for i in range(0, 5):
			row = []
			for j in range(0, 5):
				row.append(Cell())
			self.grid.append(row)

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
				x, y = pygame.mouse.get_pos()	
				if x > 375 and x < 575 and y > 460 and y < 525:
					return()
				if x > 375 and x < 575 and y > 600 and y < 665:
					pygame.quit()
		SCREEN.blit(img, (0, 0))

		mouse = pygame.mouse.get_pos()
#		if width/2 <= mouse[0] <= width/2+110 and height/2 <= mouse[1] <= height/2+40:
#			pygame.draw.rect(SCREEN, (0, 0, 0),[385, 450, 200, 70])
#		else:
#			pygame.draw.rect(SCREEN, (0, 0, 0), [385, 600, 200, 70])
#		SCREEN.blit(q_button, (width/2+25, height/2))
#
#		SCREEN.blit(start_button, (width/2+25, height/2-60))
		pygame.display.update()

def create_button():
	pass

def get_cell_color(occupied_by):
	if occupied_by == 1:
		return RED
	elif occupied_by == 2:
		return BLUE
	else:
		return GREEN

def draw_grid(grid):
	smallfont = pygame.font.SysFont('Corbel',35)
	y = 0
	for row in range(0, 5):
		x = 0
		for col in range(0, 5):
			cell = grid.grid[row][col]
			color = get_cell_color(cell.occupied_by)
			#rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
			surface = pygame.Surface((BLOCK_SIZE - 8, BLOCK_SIZE - 8))
			surface.fill(color)
			SCREEN.blit(surface, (x + 4, y + 4))
			height_text = smallfont.render(str(cell.height), True, WHITE)
			SCREEN.blit(height_text, (x + 75, y + 75))
			#overlay = pygame.Surface((BLOCK_SIZE - 16, BLOCK_SIZE - 16))
			#pygame.draw.rect(SCREEN, color, rect, 1)
			x += BLOCK_SIZE
		y += BLOCK_SIZE

def xy_to_rowcol(xy):
	x, y = xy
	row = y // BLOCK_SIZE
	col = x // BLOCK_SIZE
	return (row, col)

def main():
	global SCREEN, CLOCK
	gamestate = GameState()
	grid = Grid()
	pygame.init()
	SCREEN = pygame.display.set_mode(RES, RESIZABLE)
	#SCREEN.blit(background, (0, 0))
	CLOCK = pygame.time.Clock()

	start_menu()
	SCREEN.fill(WHITE)

	workers_placed = 0
	sidebar = pygame.image.load('sidebar.jpg')
	img_sidebar = pygame.transform.scale(sidebar,(200,750))

	while True:
		clicked = False
		draw_grid(grid)
		SCREEN.blit(img_sidebar, (751, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					return
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				row, col = xy_to_rowcol(pos)
				clicked = True
		if clicked and gamestate.phase == GameState.PLACE_WORKERS:
			grid.grid[row][col].occupied_by = gamestate.current_player
			workers_placed += 1
			if workers_placed == 2:
				gamestate.turn += 1
				gamestate.current_player = 2
				workers_placed = 0



		pygame.display.update()

if __name__ == "__main__":
	main()
