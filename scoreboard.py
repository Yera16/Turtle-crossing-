from turtle import Turtle

GAME_OVER_FONT = ("Courier", 24, "normal")
LEVEL_FONT = ("Courier", 15, "normal")
ALIGNMENT = "center"
SCORE_ALIGNMENT = (-260, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.write_level()

    def write_level(self):
        self.goto(SCORE_ALIGNMENT)
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=LEVEL_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=GAME_OVER_FONT)

    def change_level(self):
        self.level += 1
        self.clear()
        self.write_level()

