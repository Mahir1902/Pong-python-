from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

game_is_on = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
score_board = ScoreBoard()
screen.listen()

screen.onkey(paddle_r.go_up, 'Up')
screen.onkey(paddle_r.go_down, 'Down')
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, 's')

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # R paddle miss
    if ball.xcor() > 380:
        score_board.l_point()
        screen.update()
        ball.reset()

    # L paddle misses
    if ball.xcor() < -380:
        score_board.r_point()
        screen.update()
        ball.reset()



screen.exitonclick()