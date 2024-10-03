from turtle import Screen
from pongdottedline import DottedLine
from pongscoreboard import Scoreboard
from pongpaddles import Paddle
from pongball import Ball
import time

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

r_paddles = Paddle((350, 0))
l_paddles = Paddle((-350, 0))

ball = Ball()


scoreboard = Scoreboard()

dotLine = DottedLine()
dotLine.drawDottedLine()

screen.listen()
screen.onkey(r_paddles.up, "Up")
screen.onkey(r_paddles.down, "Down")
screen.onkey(l_paddles.up, "w")
screen.onkey(l_paddles.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() > 320 and ball.distance(r_paddles) < 50) or (ball.xcor() < -320 and ball.distance(l_paddles) < 50):
        ball.bounce_x()

    if ball.xcor() > 420:
        scoreboard.l_increase_score()
        ball.reset_position()
    if ball.xcor() < -420:
        scoreboard.r_increase_score()
        ball.reset_position()

    if scoreboard.l_score == 10:
        scoreboard.game_over()
        game_is_on = False
    if scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False



screen.exitonclick()












screen.exitonclick()