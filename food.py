from turtle import Turtle
import random

food_shape = "turtle"
food_shapesize = 0.5
food_color = "green"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(food_shape)
        self.penup()
        self.shapesize(stretch_len=food_shapesize, stretch_wid=food_shapesize)
        self.color(food_color)
        # self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-280, 281, 20)
        random_y = random.randrange(-280, 281, 20)

        self.goto(random_x, random_y)
