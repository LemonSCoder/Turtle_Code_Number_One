import turtle as trtl
import random

painter = trtl.Turtle()
def house():
    painter.begin_fill()
    turn_number = 0
    painter.forward(200)
    painter.right(90)
    painter.forward(400)
    turn_number +=1
    painter.right(90)
    painter.forward(300)
    door_turns = 0
    while door_turns < 4:
        painter.right(90)
        painter.forward(200)
        door_turns += 1
    painter.forward(100)
    turn_number = 0
    while turn_number < 2:
        painter.right(90)
        painter.forward(400)
        turn_number +=1
    painter.fillcolor("orange")
    painter.end_fill()
    painter.begin_fill()
    painter.fillcolor("brown")
    painter.goto(0, 210)
    painter.goto(-200, 0)
    painter.end_fill()
def family():
    painter.circle(50)
    painter.right(90)
    painter.forward(75)
    painter.right(90)
    painter.forward(50)
    painter.right(180)
    painter.forward(100)
    painter.right(180)
    painter.forward(50)
    painter.right(-90)
    painter.forward(75)
    painter.goto(painter.xcor() - 50, painter.ycor() - 100)
    painter.goto(painter.xcor() + 50, painter.ycor() + 100)
    painter.goto(painter.xcor() + 50, painter.ycor() - 100)

house()
painter.penup()
painter.hideturtle()
painter.goto(300, -150)
painter.showturtle()
painter.pendown()
family()
trtl.done()


