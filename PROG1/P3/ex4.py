import math

def distancia_entre_dois_pontos(xi, yi, xj, yj):
    distancia = math.sqrt(((xi-xj)*(xi-xj)) + ((yi-yj)*(yi-yj)))

    return distancia

# ENTRADAS --------------------------------------
circunferencia = [float(v) for v in input().split()]

m = int(input())

coordenadas = []
for i in range(m):
    c = [float(v) for v in input().split()]
    coordenadas.append(c)

# FIM DAS ENTRADAS ---------------------------
print('Os pontos a seguir estão localizados na região definida pela circunferência:')
for i in coordenadas:
    dist = distancia_entre_dois_pontos(circunferencia[1], circunferencia[2], i[0], i[1])
    raio = circunferencia[0]
    if (dist <= raio):
        print("({0:.2f}, {1:.2f})" .format(i[0], i[1]))
