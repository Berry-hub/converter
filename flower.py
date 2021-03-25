from turtle import forward, left, right, back, exitonclick, penup, pendown, shape, speed
shape("turtle")
speed(0)

right(90)
back(250)

for i in range(18): 
    for i in range(4):
        forward(100)
        left(90)
    left(20)

forward(200)

left(90)
for i in range(5):
    for i in range(30):
        forward(4)
        left(3)
    left(90)
    for i in range(30):
        forward(4)
        left(3)
    forward(60)
    left(90)

left(90)
forward(250)
left(90)

for i in range(5):
    for i in range(30):
        forward(4)
        right(3)
    right(90)
    for i in range(30):
        forward(4)
        right(3)
    forward(60)
    right(90)

exitonclick()