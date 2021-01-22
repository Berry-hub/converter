# tento program nakresli podla tvojho zadania slnko alebo kvet, neskor ho doplnim o nieco viac

odpoved = input("Chces nakreslit 'slnko' alebo 'kvet'? ")
while odpoved == 'slnko' or 'kvet':
    if odpoved == 'slnko':
        from turtle import forward, left, right, exitonclick, penup, pendown, shape
        shape("turtle")
        for i in range(18):
            for j in range(4):
                forward(150)
                left(90)
                left(20)
        exitonclick()
    elif odpoved == 'kvet':
        from turtle import forward, left, right, exitonclick, penup, pendown, shape
        shape("turtle")
        for i in range(18):
            for j in range(4):
                forward(100)
                left(90)
            left(20)
        exitonclick()
    else:
        print("Nerozumiem, musis zadat 'slnko' alebo 'kvet'!")
        odpoved = input("Chces nakreslit 'slnko' alebo 'kvet'? ")