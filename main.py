from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.random_location()
        snake.extend()
        scoreboard.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for current in snake.snakes[1:]:
        if snake.head.distance(current) < 10:
            game_on = False
            scoreboard.game_over()







screen.exitonclick()