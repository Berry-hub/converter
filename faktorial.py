def faktorial(n):
    """funkcia vypocita faktorial cisla n!"""
    if n < 0:
        print("faktorial je definovany iba pre kladne cisla")
    elif n == 0:
        print("faktorial cisla 0 je 1")
    else:
        for i in range(1,n):
            n = n * i
        return n
faktorial(7)