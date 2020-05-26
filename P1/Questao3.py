# Leitura dos pontos x e y do ponto p1
x1, y1 = input().split(" ")
x1, y1 = float(x1), float(y1)

# Leitura dos pontos x e y do ponto p2
x2, y2 = input().split(" ")
x2, y2 = float(x2), float(y2)

# Leitura dos pontos x e y do ponto p3
x3, y3 = input().split(" ")
x3, y3 = float(x3), float(y3)

# Validação dos dados
if x3 >= x1 and x3 <= x2:
    if y3 >= y1 and y3 <= y2:
        print("S")
    else:
        print("N")
else:
    print("N")

exit(0)