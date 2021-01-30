# tento program nakresli domcek o velkosti strany "a"

import turtle
import math

def domcek(a):
    turtle.left(45)
    turtle.forward(math.sqrt(2*(a**2)))
    turtle.left(90)
    turtle.forward(math.sqrt(2*(a**2))/2)
    turtle.left(90)
    turtle.forward(math.sqrt(2*(a**2))/2) 
    turtle.left(90)
    turtle.forward(math.sqrt(2*(a**2)))
    turtle.left(135)
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.right(90)
    turtle.forward(a)


domcek(10)
domcek(25)
domcek(50)
domcek(75)
domcek(100)
turtle.exitonclick()