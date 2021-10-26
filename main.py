import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # # *** or go through the walls:
    # x_cor = snake.head.xcor()
    # y_cor = snake.head.ycor()
    # if x_cor > 290 or x_cor < -290:
    #     snake.head.goto(x_cor * -1, y_cor)
    # if y_cor > 290 or y_cor < -290:
    #     snake.head.goto(x_cor, y_cor * -1)

    # Collision with tail
    # (if head collides with any segment)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
