def fibonacci(n):
    """returns first 'n' numbers of Fibonacci retracement"""
    fibo = [1, 1]
    for i in range(n-2):
		    fibo.append(fibo[-1] + fibo[-2])
    return fibo

def fibonacci_other_way(n):
    a, b = 1, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

def even_fibonacci(n):
    """returns first 'n' even numbers of Fibonacci retracement"""
    even_fibo = []
    for n in fibonacci(n):
        if n % 2 == 0:
            even_fibo.append(n)
    return even_fibo[13]
  
# print(even_fibonacci(50))
# print(fibonacci(7))
# fibonacci_other_way(20)