from random import randrange
sucet = 0
#
print("Hra OCKO, budes nahodne dostavat karty v hodnote 2-11 bodov, cielom je mat 21 bodov")
print("Zaciname, mas 0 bodov")
#
while sucet < 21:
    odpoved = input("Odpovedaj 'ano' alebo 'nie', chces kartu? ")
    if odpoved == 'ano':
        cislo = randrange(1,11)
        print("Karta je ", cislo)
        sucet = (cislo + sucet)
        print("Sucet bodov je", sucet)
        if sucet > 21:
            print("Koniec, prehral si!")
        if sucet == 21:
            print("Vyborne, vyhral si!")
    elif odpoved == 'nie':
            print("Skoda, uz len ", 21 - sucet, "a mal by si 21!")
            break
    else:
        print("Nerozumiem, odpovedaj 'ano' alebo 'nie'!")