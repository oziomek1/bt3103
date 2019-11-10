class Snake:
    def __init__(self, x_vector, y_vector):
        self.x_vector = x_vector
        self.y_vector = y_vector

    def go_up(self):
        # START CODE HERE
        if self.y_vector > 0:
            return "Going Up"
        self.y_vector = 10
        self.x_vector = 0
        return