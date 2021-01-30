import turtle
import math
#
turtle.speed(0)
turtle.left(180)
turtle.forward(450)
turtle.right(180)
#
for i in range(8):
    turtle.left(45)
    turtle.forward(math.sqrt(20000))
    turtle.left(90)
    turtle.forward(math.sqrt(20000)/2)
    turtle.left(90)
    turtle.forward(math.sqrt(20000)/2)
    turtle.left(90)
    turtle.forward(math.sqrt(20000))
    turtle.left(135)
    for j in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(90)
    turtle.forward(25)

turtle.exitonclick()