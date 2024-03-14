# Design or Use of Pen
import random
import turtle
# from turtle import Turtle,Screen
#
# tim = Turtle()
# screen = Screen()
# tim.pencolor("blue")
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def move_left():
#     tim_heading = tim.heading() + 10
#     tim.setheading(tim_heading)
#
#
# def move_right():
#     tim_heading = tim.heading() - 10
#     tim.setheading(tim_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forward, "m")
# screen.onkey(move_backward, "b")
# screen.onkey(move_left, "l")
# screen.onkey(move_right, "r")
# screen.onkey(clear, "c")
#
#
# screen.exitonclick()


from turtle import Turtle, Screen


screen = Screen()
screen.setup(500,400)
turtels = []
color = ["red","blue", "orange", "purple", "green", "yellow"]
print("The existting colors ")
for c in color:
    print(c)
direction = [-70, -40, -10, 20, 50, 80]
user_bet = screen.textinput("Make your bet","Which turtle win the race? Enter the color : ")
is_on = False
for turtle_count in range(6):

    my_new_turrtle = Turtle()
    my_new_turrtle.penup()
    my_new_turrtle.shape("turtle")
    my_new_turrtle.color(color[turtle_count])
    my_new_turrtle.goto(x=-230,y=direction[turtle_count])
    turtels.append(my_new_turrtle)
if user_bet:
    is_on = True


while is_on:
     for turtle in turtels:
         if turtle.xcor()> 230:
            winning_color = turtle.pencolor()
            is_on = False
            if user_bet==winning_color:
                 print(f"You Won!!!,{winning_color} has won the match")
            else:
                print(f"You loose , {winning_color} has won the match")

         random_distance = random.randint(0, 10)
         turtle.forward(random_distance)




screen.exitonclick()








