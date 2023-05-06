# My first project in pycharm

#import packages
#import turtle
#import random
#import time
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")


#creating border
turtle.speed(10)
turtle.pensize(4)
turtle.prenup()
turtle.goto(-310, 250)
turtle.pentdown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.prenup()
turtle.hideturtle()

# score
score = 0;
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.prenup()
snake.goto(0, 0)
snake.direction = 'stop'

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.prenup()
fruit.goto(30, 30)

old_fruit = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.prenup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))

# define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_up():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_up():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_up():
    if snake.direction != "left":
        snake.direction = "right"
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "left":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "right":
        y = snake.ycor()
        snake.sety(y + 20)

# keyboard binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "left")
screen.onkeypress(snake_go_right, "Right")

# main loop
while True:
    screen.update()

