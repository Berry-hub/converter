# hra piskvorky 1-D
# simuluje tahy pocitaca a ty zadavas svoje tahy

from random import randrange
#
def vyhodnot(pole):
    """vyhodnoti vysledok resp. stav pole"""
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"
#
def tah(pole, pozice, symbol):
    """vrati herne pole podla zadania"""
    return pole[:pozice] + symbol + pole[pozice + 1:]
#
def tah_hrace(pole):
    """spyta sa hraca, kde chce hrat a vrati herne pole so zaznamenanym tahom"""
    while True:
        pozice = int(input("Na jakou pozici chces hrat? "))
        if pozice >= 0 and pozice < len(pole) and pole[pozice] == "-":
            return tah(pole, pozice, "x")
        else:
            print("Blbe, na jakou pozici chces hrat? ")
#
def tah_hrace2(pole):
    """spyta sa hraca, kde chce hrat a vrati herne pole so zaznamenanym tahom"""
    while True:
        pozice = int(input("Na jakou pozici chces hrat? "))
        if pozice >= 0 and pozice < len(pole) and pole[pozice] == "-":
            return tah(pole, pozice, "o")
        else:
            print("Blbe, na jakou pozici chces hrat? ")            
#
def tah_pocitace(pole):
    """vrati herne pole so zaznamenanym tahom pocitaca"""
    while True:
        pozice = randrange(len(pole))
        if pole[pozice] == "-":
            return tah(pole, pozice, "o")
        else:
            return pozice
#
def piskvorky1d():
    """hra proti pocitaci (vratane nasledneho vyhodnotenia)"""
    pole = 20 * "-"
    while True:
        print(pole)
        pole = tah_hrace(pole)
        print(pole)
        if vyhodnot(pole) != "-":
            break
        pole = tah_pocitace(pole)
        if vyhodnot(pole) != "-":
            break
    print(pole)
    vyhodnot(pole)
    if "xxx" in pole:
        print("x - vyhral si")
    elif "ooo" in pole:
        print("o - vyhral pocitac")
    elif "-" not in pole:
        print("remiza")
#
def piskvorky1d2():
    """hra pre 2 hracov (vratane nasledneho vyhodnotenia)"""
    pole = 20 * "-"
    while True:
        print(pole)
        pole = tah_hrace(pole)
        print(pole)
        if vyhodnot(pole) != "-":
            break
        pole = tah_hrace2(pole)
        if vyhodnot(pole) != "-":
            break
    print(pole)
    vyhodnot(pole)
    if "xxx" in pole:
        print("x - vyhral hrac 1")
    elif "ooo" in pole:
        print("o - vyhral hrac 2")
    elif "-" not in pole:
        print("remiza")

piskvorky1d2()
