from turtle import Turtle
import random

shapes = ["circle", "square", "triangle"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(x=random_x, y=random_y)
        self.shape(self.change_shape())

    def change_shape(self):
        shape = random.choice(shapes)
        return shape