def zadaj_prvocislo():
    """vypise zoznam delitelov zadaneho cisla
        zaroven zisti, ci sa jedna o prvocislo"""
    n = int(input("zadaj akekolvek prirodzene cislo: "))
    delitel = []
    for i in range(1,n+1):
        if n % i == 0:
            delitel.append(i)
    print("delitele tvojho cisla su: ", delitel)        
    if len(delitel) == 2:
        print("jedna sa o PRVOCISLO!!!")
    if n == 1:
        print("jednotka nie je prvocislo, nema dvoch delitelov")
    elif n < 1:
        print("zadaj akekolvek prirodzene cislo")
#zadaj_prvocislo()


def prvocislo(n):
    """vypise zoznam prvocisel od 2 do n"""
    delitelnost = []
    prvocislo = []
    for i in range(2,n+1):
        for j in range(2,n+1):
            if i % j == 0:
                delitelnost.append(i)
    for cisla in delitelnost:
        if delitelnost.count(cisla) == 1:
            prvocislo.append(cisla)
    return prvocislo

#print(prvocislo(17))
