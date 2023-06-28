from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
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
screen.listen()

screen.onkey(paddle_r.go_up, 'Up')
screen.onkey(paddle_r.go_down, 'Down')
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, 's')

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()





screen.exitonclick()