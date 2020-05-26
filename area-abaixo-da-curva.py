#python 3.8
x1 = int(input("Digite o valor de x do primeiro par de valor:   "))
fx1 = int(input("Digite o valor de f(x) do primeiro par de valor:   "))

x2 = int(input("Digite o valor de x do segundo par de valor:   "))
fx2 = int(input("Digite o valor de f(x) do segundo par de valor:   "))

x3 = int(input("Digite o valor de x do terceiro par de valor:   "))
fx3 = int(input("Digite o valor de f(x) do terceiro par de valor:   "))

x4 = int(input("Digite o valor de x do quarto par de valor:   "))
fx4 = int(input("Digite o valor de f(x) do quarto par de valor:   "))

a1 = ((fx2 + fx1) * (x2 - x1)) / 2

a2 = ((fx3 +fx2) * (x3 - x2)) / 2

a3 = ((fx4 + fx3) * (x4 - x3)) / 2

at = a1 + a2 + a3

print("A area abaixo da curva obtida pela soma das tres areas de trapezio é %d" %at)

exit(0)