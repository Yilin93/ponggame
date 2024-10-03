from turtle import Turtle

pace = 20
class DottedLine:

    def drawDottedLine(self):
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.pencolor("white")
        tim.pensize(10)
        tim.goto(0, -300)
        tim.setheading(90)
        for i in range(int(600/pace)):
            tim.pendown()
            tim.forward(20)
            tim.penup()
            tim.forward(20)






