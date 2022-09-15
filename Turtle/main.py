from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.shape("turtle")
tim.color("thistle")
tim.speed(10)

colours = ["dark gray", "blue", "navy", "olive drab", "gold", "medium spring green", "yellow", "red", "green", "purple",
           "black", "pink", "dark magenta", "rebecca purple", "brown", "light salmon", "rosy brown", "forest green"]
range_num = 3
while range_num < 11:
    for _ in range(range_num):
        tim.left(360 / range_num)
        tim.forward(100)
    range_num += 1
    tim.color(choice(colours))

screen = Screen()
screen.exitonclick()
