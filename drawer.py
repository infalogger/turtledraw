import turtle
from operator import contains

import keyboard

turtledata = "turtledata.txt"

turtle.bgcolor("black")
turtle.pencolor("white")
turtle.pensize(2)
turtle.tracer(0)

with open(turtledata, "r") as f:
    for line in f:
        if contains(line, "pen") == False:
            line = line.replace("\n", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.split(",")
            print(line)

            turtle.goto(float(line[0]), float(line[1]))
        else:
            line = line.replace("\n", "")
            if line == "penup":
                turtle.penup()
            elif line == "pendown":
                turtle.pendown()
turtle.update()

while keyboard.is_pressed('q') == False:
    print("finished")
