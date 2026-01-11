import turtle
import keyboard

turtle.bgcolor("black")
turtle.pencolor("white")
turtle.pensize(2)
turtle.penup()
turtle.tracer(0)


## lower = more optimized less file size
optimizationlevel = 1

turtledata = "turtledata.txt"


with open(turtledata, "w") as f:
    f.write("")

previouspos = None

pendownsaved = False

while keyboard.is_pressed('q') == False:
    previouspos = turtle.position()
    if((keyboard.is_pressed('space'))):
        turtle.pendown()
        if pendownsaved == False:
            with open(turtledata, "a") as f:
                f.write("pendown\n")
                print("pendown")
                pendownsaved = True
    else:
        turtle.penup()
        if pendownsaved == True:
            with open(turtledata, "a") as f:
                f.write("penup\n")
                print("penup")
                pendownsaved = False
    if((keyboard.is_pressed('w'))):
        turtle.forward(.1)
    if((keyboard.is_pressed('s'))):
        turtle.backward(.1)
    if((keyboard.is_pressed('a'))):
        turtle.left(.1)
    if((keyboard.is_pressed('d'))):
        turtle.right(.1)

    if previouspos != turtle.position() and (round(previouspos[0], optimizationlevel) != round(turtle.position()[0], optimizationlevel) and round(previouspos[1], optimizationlevel) != round(turtle.position()[1]), optimizationlevel):
        print(turtle.position())
        with open(turtledata, "a") as f:
            f.write(str(turtle.position())+ "\n")
    turtle.update()