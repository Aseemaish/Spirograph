import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
my_screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


aseem = Turtle()
aseem.shape("turtle")
aseem.color("black")
aseem.speed(0)


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        aseem.color(random_color())
        aseem.circle(100)
        aseem.setheading(aseem.heading() + size_of_gap)


draw_spirograph(5)

my_screen.exitonclick()
