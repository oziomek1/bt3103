import pygame as pg
import random
import time


class Square():
	def __init__(
		self,
		cell_size,
		x_position,
		y_position,
	):
		self.cell_size = cell_size
		self.x_position = x_position
		self.y_position = y_position

	# def get_square_box(self):
	# 	return (self.x_position, self.y_position, self.cell_size, self.cell_size)


class Cell(Square):
	def __init__(
		self, 
		cell_size=20, 
		color=(255, 255, 255), 
		x_position=None, 
		y_position=None, 
		display_window=None,
	):
		# super().__init__(cell_size=cell_size, x_position=x_position, y_position=y_position)
		self.cell_size = cell_size
		self.x_position = x_position
		self.y_position = y_position
		self.color = color
		self.display_window = display_window

	def draw(self):
		# self.display_window.fill(
		# 	self.color, 
		# 	rect=[
		# 		self.x_position, 
		# 		self.y_position, 
		# 		self.cell_size, 
		# 		self.cell_size,
		# 	],
		# )
		pg.draw.rect(
			self.display_window, 
			self.color, 
			# pg.Rect(self.get_square_box()),
			pg.Rect(self.x_position, self.y_position, self.cell_size, self.cell_size),
		)


class Snake():
	def __init__(self, cell_size=20, x_position=0, y_position=0, color=(0, 0, 255), length=3, display_window=None):
		self.cell_size = cell_size
		self.x_position = x_position
		self.y_position = y_position
		self.color=color
		self.length = length
		self.display_window = display_window
		self.x_speed_current = 0
		self.y_speed_current = self.cell_size
		self.x_speed_previous = 0
		self.y_speed_previous = 0
		self.cells = [
			Cell(cell_size=self.cell_size, x_position=x_position, y_position=y_position, color=self.color, display_window=self.display_window)
			for i in range(length)
		]

	def add_cell(self):
		self.cells.append(
			Cell(cell_size=self.cell_size, x_position=self.cells[-1].x_position, y_position=self.cells[-1].y_position, color=self.color, display_window=self.display_window)
		)

	def turn_left(self):
		if self.x_speed_current > 0:
			return
		self.x_speed_current = -self.cell_size
		self.y_speed_current = 0

	def turn_right(self):
		if self.x_speed_current < 0:
			return
		self.x_speed_current = self.cell_size
		self.y_speed_current = 0

	def turn_down(self):
		if self.y_speed_current < 0:
			return 
		self.y_speed_current = self.cell_size
		self.x_speed_current = 0

	def turn_up(self):
		if self.y_speed_current > 0:
			return 
		self.y_speed_current = -self.cell_size
		self.x_speed_current = 0

	def draw(self):
		for cell in self.cells:
			cell.draw()

	def calculate_new_cell_positions(self):
		return (
			self.cells[0].x_position + self.x_speed_current, 
			self.cells[0].y_position + self.y_speed_current,
		)

	def move(self):
		x_position_new, y_position_new = self.calculate_new_cell_positions()

		self.cells.pop()
		self.cells.insert(
			0, 
			Cell(cell_size=self.cell_size, x_position=x_position_new, y_position=y_position_new, color=self.color, display_window=self.display_window),
		)


class Snack():
	def __init__(self, cell_size=20, x_position_max=0, y_position_max=0, color=(0, 255, 0), display_window=None):
		self.cell_size = cell_size
		self.x_position_max = x_position_max
		self.y_position_max = y_position_max
		self.x_position = 0
		self.y_position = 0
		self.color = color
		self.display_window = display_window
		self.calculate_and_assign_position()

	def round_down(self, position):
		return position - (position % self.cell_size)

	def calculate_and_assign_position(self):
		self.x_position = self.round_down(random.randint(0, self.x_position_max))
		self.y_position = self.round_down(random.randint(0, self.y_position_max))
		self.snack_cell = Cell(cell_size=self.cell_size, x_position=self.x_position, y_position=self.y_position, color=self.color, display_window=self.display_window)

	def draw(self):
		self.snack_cell.draw()

	def reassign(self):
		self.calculate_and_assign_position()
		

class Game():
	def __init__(self, window_width=600, window_height=400, cell_size=20, moving_rate=10):
		self.window_width = window_width
		self.window_height = window_height
		self.cell_size = cell_size
		self.moving_rate = moving_rate

		pg.init()
		self.display_window = pg.display.set_mode((window_width, window_height))
		self.clock = pg.time.Clock()
		self.font = pg.font.SysFont('console', 48, False)
		self.fps = 25
		self.failed = False
		self.ticks = None
		self.reset()
	
	def start(self):
		self.clock.tick(self.fps)
		rate_counter = 0
		while True:
			time.sleep(0.001)
			self.catch_event()
			self.display_window.fill(pg.Color('black'))
			self.draw()
			pg.display.update()

			if rate_counter % self.moving_rate == 0:
				self.snake.move()
				rate_counter = 0

				self.check_collide()
				if self.check_eat():
					self.snake.add_cell()
					self.snack.reassign()
					self.check_correct_snack_position()

				if self.failed:
					self.draw_failure()
					self.reset()
					self.failed = False
					self.show_menu()
			rate_counter += 1


	def show_menu(self):
		self.clock.tick(self.fps)
		button_play_x = self.window_width // 5
		button_play_y = 2 * self.window_height // 3
		button_quit_x = self.window_width - 2 * self.window_width // 5
		button_quit_y = 2 * self.window_height // 3
		button_width = self.window_width // 5
		button_height = self.window_height // 5
		while True:
			time.sleep(0.001)
			click_position = self.catch_menu_event()
			if click_position:
				if button_play_y <= click_position[1] <= button_play_y + button_height:
					if button_play_x <= click_position[0] <= button_play_x + button_width:
						break
					if button_quit_x <= click_position[0] <= button_quit_x + button_width:
						pg.quit()
			self.display_window.fill(pg.Color('black'))
			self.display_window.blit(self.font.render('Menu', False, pg.Color('gray')), (self.window_width // 2.5, self.window_height // 3))
			pg.draw.rect(
				self.display_window, 
				pg.Color('darkgreen'), 
				pg.Rect(button_play_x, button_play_y, button_width, button_height),
			)
			pg.draw.rect(
				self.display_window, 
				pg.Color('darkred'), 
				pg.Rect(button_quit_x, button_quit_y, button_width, button_height),
			)
			self.display_window.blit(
				self.font.render('Play', False, pg.Color('gray')), 
				(button_play_x + self.cell_size // 2, button_play_y + self.cell_size // 2),
			)
			self.display_window.blit(
				self.font.render('Quit', False, pg.Color('gray')), 
				(button_quit_x + self.cell_size // 2, button_quit_y + self.cell_size // 2),
			)
			pg.display.update()


	def catch_event(self):
		for event_getter in pg.event.get():
			try:
				if event_getter.type == pg.KEYDOWN:
					key = event_getter.key
					for event in self.prepare_events():
						if event['event_action'] == key:
							event['event_result']()
			except Exception as e:
				print(e)

	def catch_menu_event(self):
		for event_getter in pg.event.get():
			try:
				if event_getter.type == pg.MOUSEBUTTONDOWN:
					x, y = event_getter.pos
					return (x, y)
			except Exception as e:
				print(e)

	def check_collide(self):
		head = self.snake.cells[0]
		for index, snake_cell in enumerate(self.snake.cells):
			if snake_cell.x_position < 0 or snake_cell.x_position >= self.window_width or \
			   snake_cell.y_position < 0 or snake_cell.y_position >= self.window_height:
				self.failed = True
				return
			if index > 0 and snake_cell.x_position == head.x_position and snake_cell.y_position == head.y_position:
				self.failed = True
				return

	def check_correct_snack_position(self):
		for snake_cell in self.snake.cells:
			if snake_cell.x_position == self.snack.x_position and snake_cell.y_position == self.snack.y_position:
				self.snack.reassign()
				return self.check_correct_snack_position()

	def check_eat(self):
		if self.snake.cells[0].x_position == self.snack.x_position and self.snake.cells[0].y_position == self.snack.y_position:
			return True
		return False

	def draw(self):
		self.snake.draw()
		self.snack.draw()

	def draw_failure(self):
		self.display_window.blit(self.font.render('Failed', False, pg.Color('red')), (self.window_width // 3, self.window_height // 2))
		pg.display.update()
		# pg.event.pump()
		# pg.time.wait(1000)

	def prepare_events(self):
		return [
			{
				'event_action': pg.K_LEFT,
				'event_result': self.snake.turn_left,
			},
			{
				'event_action': pg.K_RIGHT,
				'event_result': self.snake.turn_right,
			},
			{
				'event_action': pg.K_UP,
				'event_result': self.snake.turn_up,
			},
			{
				'event_action': pg.K_DOWN,
				'event_result': self.snake.turn_down,
			},	
		]

	def reset(self):
		self.display_window.fill(pg.Color('black'))
		self.snake = Snake(
			self.cell_size, 
			x_position = self.window_width // 2,
			y_position = self.window_height // 2,
			display_window = self.display_window,
		)
		self.snack = Snack(cell_size=self.cell_size, x_position_max=self.window_width, y_position_max=self.window_height, display_window=self.display_window)
		self.check_correct_snack_position()

def initialize():
	game = Game(moving_rate=10)
	game.show_menu()
	game.start()


initialize()
