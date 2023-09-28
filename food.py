from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        # init the parent class
        super().__init__()
        self.penup()
        self.color("purple")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
