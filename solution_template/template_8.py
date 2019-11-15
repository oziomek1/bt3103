class Cell:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

class Snake:
    def __init__(self):
        self.cells = [Cell(0,0), Cell(1,1)]

class Game:
    def __init__(self, snake, snack):
        self.snake = snake
        self.snack = snack

    def check_eat(self):
        ##START CODE HERE##