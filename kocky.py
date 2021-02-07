# hra kocky
from random import randrange
#
print("Hraci budu hadzat kockou, kym nepadne 6 - vyhrava ten, kto potreboval na jej hodenie najviac hodov.")
#
def hra(hrac):
    """funkcia simuluje nahodne hody kockou, pri hodeni 6 hra konci, pocita pocet kol"""
    print("Hraje hrac: ", hrac)
    hod = randrange(1,7) # nahodny hod kockou, vyberie cislo od 1 po 6
    kolo = 1
    while hod != 6:
        print("Hrac hodil:", hod,", kolo", kolo)
        hod = randrange(1,7)
        kolo += 1
    if hod == 6:
        print("Hrac hodil:", hod,", kolo", kolo)
    print("Hra skoncila v kole", kolo)
    return kolo # vracia hodnotu pre neskorsie vyhodnotenie v dalsej funkcii
#
def vyhodnotenie(vysledok_1, vysledok_2, vysledok_3):
    """funkcia vyhodnocuje vysledky vyssie definovanej hry,
        je mozne ju prepisat na iny pocet hracov"""
    if vysledok_1 >= vysledok_2 and vysledok_1 >= vysledok_3:
        print("Vyhral hrac 1!")
    elif vysledok_2 > vysledok_1 and vysledok_2 >= vysledok_3:
        print("Vyhral hrac 2!")
    else:
        print("Vyhral hrac 3!")
#
vyhodnotenie(hra(1),hra(2),hra(3))

