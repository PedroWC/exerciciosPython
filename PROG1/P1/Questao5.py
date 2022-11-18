# Leitura dos quatro pontos 
# Ponto 1
x1, y1  = input().split(" ")
x1, y1 = int(x1), int(y1)
# Ponto 2
x2, y2  = input().split(" ")
x2, y2 = int(x2), int(y2)
# Ponto 3
x3, y3  = input().split(" ")
x3, y3 = int(x3), int(y3)
# Ponto 4
x4, y4  = input().split(" ")
x4, y4 = int(x4), int(y4)

# Cálculos das bases e da altura
base_menor = x2 - x1
base_maior = x3 - x4
altura = y1 - y4

# Cálculo da área
area =  ((base_maior + base_menor) * altura ) / 2

# Impressão da área
print("{0:.2f}" .format(area))

exit(0)