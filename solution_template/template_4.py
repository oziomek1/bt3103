class Cell():
    def __init__(self,cell_size=20,color=(255, 255, 255),x_position=None,y_position=None):

        self.cell_size = cell_size
        self.x_position = x_position
        self.y_position = y_position
        self.color = color

class Snake():
    def __init__(self, cell_size=20, x_position=0, y_position=0, color=(0, 0, 255), length=3):
        self.cell_size = cell_size
        self.x_position = x_position
        self.y_position = y_position
        self.color=color
        self.length = length
        self.cells = [
            Cell(cell_size=self.cell_size, x_position=x_position, y_position=y_position, color=self.color) for i in range(length)]

    def add_cell(self):
        self.cells.append(
            Cell(cell_size=self.cell_size, x_position=self.cells[-1].x_position, y_position=self.cells[-1].y_position, color=self.color))
        # START CODE HERE