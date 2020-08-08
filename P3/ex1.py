meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

matriz = []
vetor = []
for i in range(4):
    linha = []
    linha = input().split()
    matriz.append(list(map(int, linha)))

total = 0
for i in range(4):
    total = 0
    for j in range(6):
        total = total + matriz[i][j]
    print(total, end=' ')
    vetor.append(total)

print()

total_mes = 0
for j in range(6):
    total_mes = 0
    for i in range(4):
        total_mes = total_mes + matriz[i][j]
    if j == 5:
        print(total_mes, end='\n')
    else:
        print(total_mes, end=' ')

menor = min(vetor)
indice = vetor.index(menor)

menorVenda = matriz[0][0]
for i in matriz:
    for e in i:
        if e < menorVenda:
            menorVenda = e
            X = i.index(e)
            Y = matriz.index(i)

print(f'Loja {indice+1}')
print("Mês de menor venda: {}. Loja {}".format(meses[X], Y+1))
