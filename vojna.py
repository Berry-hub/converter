# vojna - kartova hra

from random import shuffle

karty = []
for karta in list(range(7,15)):
    for znak in range(4):
        karty.append(karta)
shuffle(karty)
moj_prvy_balicek = karty[:16]
pocitacov_prvy_balicek = karty[16:]
print("moje karty:", moj_prvy_balicek,
        "karty pocitaca:", pocitacov_prvy_balicek)
def tah():
    while len(moj_prvy_balicek) > 3 and len(pocitacov_prvy_balicek) > 3:
        odpoved = input("stlac enter ")
        shuffle(moj_prvy_balicek), shuffle(pocitacov_prvy_balicek)
        print("ja:", moj_prvy_balicek[0], "pocitac:", pocitacov_prvy_balicek[0])
        if moj_prvy_balicek[0] > pocitacov_prvy_balicek[0]:
            moj_prvy_balicek.append(pocitacov_prvy_balicek[0])
            pocitacov_prvy_balicek.remove(pocitacov_prvy_balicek[0])
        elif moj_prvy_balicek[0] < pocitacov_prvy_balicek[0]:
            pocitacov_prvy_balicek.append(moj_prvy_balicek[0])
            moj_prvy_balicek.remove(moj_prvy_balicek[0])
        elif moj_prvy_balicek[0] == pocitacov_prvy_balicek[0]:
            print("VOJNA!")
            print("ja:", moj_prvy_balicek[1:3], moj_prvy_balicek[3])
            print("pocitac:", pocitacov_prvy_balicek[1:3], pocitacov_prvy_balicek[3])
            if moj_prvy_balicek[3] > pocitacov_prvy_balicek[3]:
                for i in range(4):
                    moj_prvy_balicek.append(pocitacov_prvy_balicek[0])
                    pocitacov_prvy_balicek.remove(pocitacov_prvy_balicek[0])
            elif moj_prvy_balicek[3] < pocitacov_prvy_balicek[3]:
                for i in range(4):
                    pocitacov_prvy_balicek.append(moj_prvy_balicek[0])
                    moj_prvy_balicek.remove(moj_prvy_balicek[0])
            elif moj_prvy_balicek[3] == pocitacov_prvy_balicek[3]:
                print("ja:", moj_prvy_balicek[4:6], moj_prvy_balicek[6])
                print("pocitac:", pocitacov_prvy_balicek[4:6], pocitacov_prvy_balicek[6])
                if moj_prvy_balicek[6] > pocitacov_prvy_balicek[6]:
                    for i in range(7):
                        moj_prvy_balicek.append(pocitacov_prvy_balicek[0])
                        pocitacov_prvy_balicek.remove(pocitacov_prvy_balicek[0])
                elif moj_prvy_balicek[6] < pocitacov_prvy_balicek[6]:
                    for i in range(7):
                        pocitacov_prvy_balicek.append(moj_prvy_balicek[0])
                        moj_prvy_balicek.remove(moj_prvy_balicek[0])
        if odpoved == "show":
            print("moje karty:", moj_prvy_balicek,
                   "karty pocitaca:", pocitacov_prvy_balicek)
        
    if len(moj_prvy_balicek) <= 3:
        print("KONIEC! Prehral si!")
    elif len(pocitacov_prvy_balicek) <= 3:
        print("KONIEC! Vyhral si!")

tah()