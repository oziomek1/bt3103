class Cell():  # we are omitting (Square) to make the code run smoothly
    def __init__(
        self,
        cell_size = ,
        color = ,  #RGB value for the color white
        x_position=None,
        y_position=None,
        # DON'T FORGET TO ADD DISPLAY_WINDOW
        ):
 
        self.cell_size = cell_size
        self.x_position = x_position
        self.y_position = y_position
        self.color = color
        
 
#     def draw(self):
#         pg.draw.rect(
#             self.display_window,
#             self.color,
#             pg.Rect(self.x_position, self.y_position, self.cell_size, self.cell_size)
