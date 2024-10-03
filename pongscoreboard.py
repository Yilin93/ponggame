from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self, ):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.updated_score()


    def updated_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)


    def l_increase_score(self):
        self.l_score += 1
        self.updated_score()


    def r_increase_score(self):
        self.r_score += 1
        self.updated_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)

