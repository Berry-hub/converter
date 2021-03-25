from turtle import forward, back, left, right, speed, exitonclick
speed(0)

for i in range(8):
    for i in range(5):
        forward(30)
        left(45)
        forward(30)
        back(30)
        right(90)
        forward(30)
        back(30)
        left(45)
    back(150)
    right(45)

exitonclick()