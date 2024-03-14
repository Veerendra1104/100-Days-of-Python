import time

from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("M S Games")
screen.tracer(0)
positions = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()

food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




is_on = True

while is_on:
    screen.update()
    time.sleep(1)
    snake.move()

    #Detect the collusion of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect thecollusion to the edge
    if snake.head.xcor() >290 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on= False
        scoreboard.game_over()

    #Detect the collusion of snake touch to tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            scoreboard.game_over()

screen.exitonclick()