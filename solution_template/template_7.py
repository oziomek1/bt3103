class Cell:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

class Snake:
    def __init__(self):
        self.cells = []

class Game:
    def __init__(self, snake):
        self.failed = False
        self.window_width = 100
        self.window_height = 100
        self.snake = snake

    def check_collide(self):
        ##START CODE HERE##