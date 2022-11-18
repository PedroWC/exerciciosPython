# Factorial numbers module
# Not extracted from any official documentation

#inicialization of auxiliary number 'num'
num = 0

def fat(n):    # Write result of Factorial number
    while n > 0:
        num = n
        fatorial = 1
        while n > 1:
            fatorial *= n
            n -= 1
    print("{}! = {}" .format(num, fatorial))

def fat2(n):    # Return reult of Factrial number in a list
    while n > 0:
        fatorial = 1
        while n > 1:
            fatorial *= n
            n -= 1
        return fatorial