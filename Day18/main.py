import random

import turtle as t
from turtle import Screen
# my_new_turttle = Turtle()
# movement =0
#
# while movement<=3:
#     my_new_turttle.shape("triangle")
#     my_new_turttle.color("blue")
#     my_new_turttle.forward(100)
#     my_new_turttle.right(90)
#     movement +=1
#
#
# ............................Spirogram.................................
# tim = t.Turtle()
# colors = ["blue","green","red","yellow","greenyellow","pink","orange","black","gray"]
#
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(angle)
#
#
#
#
# for shape_sides in range(3,11):
#     t.color(random.choice(colors))
#     draw_shape(shape_sides)
#
#
# tim = t.Turtle()
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0 , 255)
#     b = random.randint(0, 255)
#     return  (r , g, b)
#
# tim.speed("fastest")
#
# def draw_spirogram(size):
#     for _ in range(int(360/size)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size)
#
#
# draw_spirogram(5)


# ................Colors_Picture...........................

import colorgram
#
# rgb_color = []
# colors = colorgram.extract("colors.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
#
# print(rgb_color)

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colors = [(26, 20, 13), (33, 19, 25), (18, 24, 36), (13, 31, 20), (239, 231, 219), (40, 106, 156), (179, 8, 64),
          (120, 89, 61), (199, 160, 91), (27, 139, 105), (155, 162, 169), (179, 141, 45), (110, 85, 97), (234, 212, 93),
          (11, 91, 51), (52, 34, 124), (11, 165, 189), (160, 209, 241), (238, 161, 181), (109, 100, 167), (93, 175, 67),
          (166, 145, 151), (144, 162, 136), (250, 226, 0), (246, 228, 234), (204, 208, 207), (82, 75, 27), (3, 81, 111),
          (143, 204, 234), (156, 105, 129)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










screen = Screen()
screen.exitonclick()
