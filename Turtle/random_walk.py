import turtle
from turtle import Turtle, Screen
from random import choice, randint
from random import randint
tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.pensize(8)
turtle.colormode(255)


# colours = ["dark gray", "blue", "navy", "olive drab", "gold", "medium spring green", "yellow", "red", "green", "purple",
#            "black", "pink", "dark magenta", "brown", "light salmon", "rosy brown", "forest green"]

random_turn_options = [90, 180, 270, 360]


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    ran_colour = (r, g, b)
    return ran_colour


def random_walk_orders():
    tim.forward(20)
    tim.left(choice(random_turn_options))
    tim.color(random_colour())


for _ in range(200):
    random_walk_orders()


screen = Screen()
screen.exitonclick()
