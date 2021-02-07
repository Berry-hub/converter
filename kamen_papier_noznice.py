# hra kamen/papier/noznice

from random import randrange
#
print("Ideme hrat hru kamen/papier/noznice." + "\n"
+ "Ak budes chces skoncit, napis 'koniec'.")
#
while True:
    odpoved = input("Co chces hrat? Napis: 'kamen', 'papier' alebo 'noznice': ")
    if odpoved == 'koniec':
        break
#         
    print("pocitac:", end=" ")
    cislo = randrange(3)
    if cislo == 0:
        print("kamen") 
    elif cislo == 1:
        print("papier")
    elif cislo == 2:
        print("noznice")
    #
    print("vysledok:", end=" ")
    if (odpoved == 'kamen' and cislo == 0) or (odpoved == 'papier' and cislo == 1) or (odpoved == 'noznice' and cislo == 2):
        print("Remiza!")
    elif (odpoved == 'kamen' and cislo == 1) or (odpoved == 'papier' and cislo == 2) or (odpoved == 'noznice' and cislo == 0):
        print("Prehral si!")
    elif (odpoved == 'kamen' and cislo == 2) or (odpoved == 'papier' and cislo == 0) or (odpoved == 'noznice' and cislo == 1):
        print("Vyhral si!")
    else:
        print("Nerozumiem tvojmu vyberu, zadaj 'kamen', 'papier' alebo 'noznice': ")