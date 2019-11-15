class Cell():  # we are omitting (Square) to make the code run smoothly
    def __init__(
        self,
        cell_size=20,
        color=(255, 255, 255),  #RGB value for the color white
        x_position=None,
        y_position=None,
        display_window=None):
 
        self.cell_size = cell_size
        self.x_position = x_position
        self.y_position = y_position
        self.color = color
        self.display_window = display_window
 
    def draw(self):
        return "Drawn Successfully"

class Test():
    def __init__(self, cell):
        self.cell = cell

    def copy(self):
        # START CODE HERE