# from turtle import Turtle, Screen
#from=keyword, turtle=modulename, import = keyword, Turtle = Thing in Module
# tim = Turtle()
# tim.shape("turtle")
#  tim.color("red" , "green")
# tim.shape("turtle")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# screen = Screen()
# screen.exitonclick()
# we can also write like this:
# import turtle as t ,here all are same but t is alias name here if we do it turtle will be count as t in all,
# and we don't have to write turtle every single time we can just write t instead if turtle.

# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()


# import heroes
# print(heroes.gen())


# import villains

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# colours = ["medium blue","sea green" ,"midnight blue" ,"lime green" ,"light salmon" ,"red" ,"saddle brown" ,"magenta"]

def random_color():
    r =random.randint(0 , 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r , g , b)
    return color

# direction = [0 , 90 , 180 , 270]
# tim.pensize(15)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# def draw_shape(num_sides):
#    for _ in range(num_sides):
#        angle = 360 / num_sides
#        tim.forward(100)
#        tim.right(angle)
#
# for shape_side_n in range(3 , 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)



# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):

       tim.color(random_color())
       tim.circle(100)
       tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


