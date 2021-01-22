from turtle import *
speed(0)
color('black', 'yellow')
def slnko (velkost):
    for i in range(9):
        for j in range(4):
            forward(velkost)
            left(90)
            left(20)
begin_fill()
slnko(300)
end_fill()
penup()
left(45)
forward(180)
pendown()
def oko (polomer):
    for i in range(360):
        forward(polomer)
        left(1)
#
color('black', 'black')
begin_fill()
oko(1/3)
end_fill()
penup()
#
right(49)
forward(65)
pendown()
#
begin_fill()
oko(1/3)
end_fill()
exitonclick()
