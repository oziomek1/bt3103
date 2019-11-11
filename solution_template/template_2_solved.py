class Cell():  # we are omitting (Square) to make the code run smoothly
    def __init__(
        self,
        cell_size = 30,
        color = (0,0,0),  #RGB value for the color white
        x_position=None,
        y_position=None,
        # DON'T FORGET TO ADD DISPLAY_WINDOW
        display_window=1,
        ):

        self.cell_size = cell_size
        self.x_position = x_position
        self.y_position = y_position
        self.color = color
        self.display_window = display_window