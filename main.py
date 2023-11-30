from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PingPongs | Artjoms L., Jaroslav B., Juliana B., Angelina B. 9c")
screen.tracer(0)
screen.listen()

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

print ('Artjoms L. 9c, Jaroslav B. 9c, Juliana B. 9c, Angelina B. 9c')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.player_2_points()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.player_1_points()

screen.exitonclick()
