# quantidade de linhas
m = int(input())
# quantidade de colunas
n = int(input())

matriz = []

# 1 lê linhas da matriz
for i in range(m):
    # 1.1 lê colunas da linha i e os tranforma em inteiros
    linha = [int(v) for v in input().split(' ')]
    # 1.2 adiciona linha à matriz
    matriz.append(linha)

# 2 conta linhas nulas
# inicializa contador de linhas nulas
linhas_nulas = 0
# 2.1 percorre m linhas
for i in range(m):
    # começa supondo que a linha é nula
    # se não for subtrai de linhas_nulas
    linhas_nulas += 1
    # 2.2 percorre n colunas
    for j in range(n):
        # 2.3 se algum elemento da linha i for diferente de 0
        if (matriz[i][j] != 0):
            # quer dizer que a linha não é nula
            linhas_nulas-= 1
            # para o laço do segundo for
            # ou seja, ja que a linha não é mais nula
            # não precisa terminar de verifica-la
            break

# 3 conta colunas nulas
# inicializa contador de colunas nulas
colunas_nulas = 0
# 3.1 percorre n colunas
for j in range(n):
    # começa supondo que a coluna é nula
    # se não for subtrai de colunas_nulas
    colunas_nulas += 1
    # 3.2 percorre m linhas
    for i in range(m):
        # 3.3 se algum elemento da coluna j for diferente de 0
        if (matriz[i][j] != 0):
            # quer dizer que a coluna não é nula
            colunas_nulas-= 1
            # para o laço do segundo for
            # ou seja, ja que a coluna não é mais nula
            # não precisa terminar de verifica-la
            break


print(f'A tem {linhas_nulas} linhas nulas e {colunas_nulas} colunas nulas')