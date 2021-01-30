# prvocislo
# program zatial NEPOCITA spravne

n = int(input("zadaj akekolvek prirodzene cislo: "))
for i in range(1,n):
    if n % i == 0:
        if i != 1 and i != n:
            print("nejedna sa o prvocislo")
            break
    elif n % i != 0:
        print("jedna sa o prvocislo")
        break
if n == 1:
    print("jednotka nie je prvocislo, nema dvoch delitelov")
elif n < 1:
    print("zadaj akekolvek prirodzene cislo")