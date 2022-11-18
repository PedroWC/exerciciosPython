# Fibonacci numbers module
# Extraído da documentação oficial de python 3

def fib(n):    # Write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()

def fib2(n):   # Return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result