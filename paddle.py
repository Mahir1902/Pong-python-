from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def go_up(self):
        new_y = self.y_pos + 20
        self.goto(self.x_pos, new_y)
        self.y_pos = new_y

    def go_down(self):
        new_y = self.y_pos - 20
        self.goto(self.x_pos, new_y)
        self.y_pos = new_y
