from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.color('black')
        self.level=0
        self.update_level()




    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}",font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over!",align="center",font=FONT)

