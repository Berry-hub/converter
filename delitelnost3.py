# tento program zisti, ci je cislo delitelne zadanym delitelom

cislo = int(input("zadaj akekolvek cele cislo: "))
delitel = int(input("zadaj delitela: "))
if cislo % delitel == 0:
    print("ano, cislo je delitelne delitelom")
else:
    print("nie, cislo nie je delitelne delitelom")
