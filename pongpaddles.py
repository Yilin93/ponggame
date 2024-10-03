from turtle import Turtle

PACE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)


    def up(self):
        y = self.ycor()
        self.sety(y+PACE)

    def down(self):
        y = self.ycor()
        self.sety(y - PACE)


