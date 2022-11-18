#python 3.8
x = int (input("Insira o valor de X   "))
y = int(input("Insira o valor de Y   "))

if( x > 0 and y > 0):
    print("O valor esta no primeiro quadrante")
elif( x> 0 and y < 0):
    print("O valor esta no segundo quadrante")
elif( x < 0 and y < 0):
    print("O valor esta no terceiro quadrante")
elif(x < 0 and y > 0):
    print("O valor esta no quarto quadrante")
elif(x != 0):
    print("O valor esta no eixo Y")
elif( y == 0):
    print("O valor esta na origem")
else:
    print("O valor esta no eixo X")
exit(0)
