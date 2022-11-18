def posicao(i: int, j: int) -> int:
    if (j == 0) or (j == i):
        return 1

    else:
        return int(posicao(i - 1, j - 1)) + int(posicao(i - 1, j))


def pascal(linhas: int) -> list:
    linhas = linhas + 1
    triangulo = []

    for linha in range(linhas):
        valores = []
        for coluna in range(linha + 1):
            valores.append(posicao(linha, coluna))

        triangulo.append(valores)

    return triangulo

n = int(input())

for i in pascal(n):
    aux1 = 0 # contador de valores
    aux2 = (len(i) - 1)  # posição do ultimo valor da linha
    
    for e in i:
        if (aux1 == aux2):
            print(e, end='\n')
            aux1 = 0
        else:
            print(e, end=" ")
            aux1 += 1

exit(0)