from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setup(width=800, height=600)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 50:
        ball.x_bounce()

    if ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.x_bounce()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
