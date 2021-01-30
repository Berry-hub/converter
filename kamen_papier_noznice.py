# hra kamen/papier/noznice

from random import randrange
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
print("ja:", end=" ")   
cislo_2 = randrange(3)
if cislo_2 == 0:
    print("kamen") 
elif cislo_2 == 1:
    print("papier")
elif cislo_2 == 2:
    print("noznice")
#
print("vysledok:", end=" ")
if (cislo == 0 and cislo_2 == 0) or (cislo == 1 and cislo_2 == 1) or (cislo == 2 and cislo_2 == 2):
    print("Remiza!")
elif (cislo == 0 and cislo_2 == 1) or (cislo == 1 and cislo_2 == 2) or (cislo == 2 and cislo_2 == 0):
    print("Vyhral som!")
else:
    print("Vyhral pocitac!")