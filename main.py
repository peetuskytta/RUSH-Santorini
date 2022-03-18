import pygame
from pygame.locals import *
from enum import Enum

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

class Command:
	SELECT_WORKER = 0
	MOVE = 1
	BUILD = 2
	def __init__(self):
		self.stage = Command.SELECT_WORKER
		self.from_cell = None
		self.to_cell = None
		self.build_cell = None

	def next_stage(self):
		self.stage += 1

class GameState:
	PLACE_WORKERS = 0
	MIDGAME = 1
	GAMEOVER = 2
	def __init__(self):
		self.phase = GameState.PLACE_WORKERS
		self.number_of_players = 2
		self.turn = 0
		self.current_player = 1
		#self.players == [Player(), Player()]

	def next_turn(self):
		self.turn += 1
		self.current_player += 1
		if self.current_player > self.number_of_players:
			self.current_player = 1

class Cell:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.height = 0
		self.occupied_by = 0

	def get_rowcol(self):
		return (self.row, self.col)

	def get_player(self):
		return (self.occupied_by)

	def is_adjacent(self, other):
		if self.row == other.row - 1 and self.col == other.col - 1: return True
		if self.row == other.row - 1 and self.col == other.col: return True
		if self.row == other.row - 1 and self.col == other.col + 1: return True
		if self.row == other.row and self.col == other.col - 1: return True
		if self.row == other.row and self.col == other.col + 1: return True
		if self.row == other.row + 1 and self.col == other.col - 1: return True
		if self.row == other.row + 1 and self.col == other.col: return True
		if self.row == other.row + 1 and self.col == other.col + 1: return True
		return False

def is_valid_move(from_cell, to_cell):
	if to_cell.height >= 4:
		return False
	if from_cell.occupied_by != 0:
		return False
	if to_cell.height > from_cell.height + 1:
		return False
	if not to_cell.is_adjacent(from_cell):
		return False
	return True

def is_valid_build(build_cell, worker_cell):
	if build_cell.occupied_by != 0:
		return False
	if build_cell.height >= 4:
		return False
	if not worker_cell.is_adjacent(build_cell):
		return False
	return True

class Grid:
	def __init__(self):
		self.grid = []
		for i in range(0, 5):
			row = []
			for j in range(0, 5):
				row.append(Cell(i, j))
			self.grid.append(row)

	def get_cell(self, row, col):
		return self.grid[row][col]

	def has_worker_at(self, row, col, current_player):
		if self.grid[row][col].occupied_by == current_player:
			return True
		return False

	def update_with_command(self, command):
		worker_row, worker_col = command.from_cell.get_rowcol()
		new_row, new_col = command.to_cell.get_rowcol()
		player = command.from_cell.get_player()
		self.grid[worker_row][worker_col].occupied_by = 0
		self.grid[new_row][new_col].occupied_by = player


def end_game(end_player):
    pass

    winner = largefont.render('PLAYER XX WINS', True, DARK)
    #state = pygame.mouse.get_pressed()
    SCREEN.blit(winner, (width/2, height/2))



# Start menu which returns true until clicked START button
def start_menu():

	# menu background
	background = pygame.image.load("santorini_menu.jpg")
	img = pygame.transform.scale(background,(950, 750))

	# Fonts
	smallfont = pygame.font.SysFont('Corbel',35)
	largefont = pygame.font.SysFont('Corbel',100)

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
			if event.type == pygame.MOUSEBUTTONUP:
				x, y = pygame.mouse.get_pos()
				if x > 375 and x < 575 and y > 460 and y < 525:
					return()
				if x > 375 and x < 575 and y > 600 and y < 665:
					pygame.quit()
		SCREEN.blit(img, (0, 0))

		mouse = pygame.mouse.get_pos()
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
	CLOCK = pygame.time.Clock()

	start_menu()
	SCREEN.fill(WHITE)

	workers_placed = 0
	command = Command()
	sidebar = pygame.image.load('sidebar.jpg')
	img_sidebar = pygame.transform.scale(sidebar,(200,750))

	while True:
		draw_grid(grid)
		SCREEN.blit(img_sidebar, (751, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					start_menu()
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				row, col = xy_to_rowcol(pos)
				if gamestate.phase == GameState.PLACE_WORKERS:
					grid.grid[row][col].occupied_by = gamestate.current_player
					workers_placed += 1
					if workers_placed == 2:
						gamestate.next_turn()
						if gamestate.current_player == 1:
							gamestate.phase = GameState.MIDGAME
						workers_placed = 0
				if gamestate.phase == GameState.MIDGAME:
					if command.stage == Command.SELECT_WORKER:
						if grid.has_worker_at(row, col, gamestate.current_player):
							command.from_cell = grid.get_cell(row, col)
							command.next_stage()
					elif command.stage == Command.MOVE:
						if is_valid_move(grid.get_cell(row, col), command.from_cell):
							command.to_cell = grid.get_cell(row, col)
							grid.update_with_command(command)
							command.next_stage()
					elif command.stage == Command.BUILD:
						command.build_cell = grid.get_cell(row, col)
						if is_valid_build(command.build_cell, command.to_cell):
							command.build_cell.height += 1
							gamestate.next_turn()
							command = Command()
		pygame.display.update()

if __name__ == "__main__":
	main()
