import turtle
speed(0)
def slnko (velkost, farba_ciary, farba_vyplne):
    """Nakresli slnko, zadaj jeho velkost, farbu ciary a vyplne"""
    color(farba_ciary, farba_vyplne)
    for i in range(9):
        for j in range(4):
            forward(velkost)
            left(90)
            left(20)
begin_fill()
slnko(300, 'red', 'yellow')
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
