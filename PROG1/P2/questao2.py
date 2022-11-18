# variável 'infinito' recebe um valor aleatório para criar um loop infinito
infinito = 100
# estrutura de repetição utilizada para criar um loop infinito
# o loop infinito é necessário pois o URI diz que: "A entrada termina com fim de arquivo"
while (infinito > 0):

    # leitura do numero de linhas e colunas da matriz
    M, N = input().split()
    M, N = int(M), int(N)

    # inicialização das variáveis 'produtividade' e 'saca'
    produtividade = 0
    saca = 0

    # inicialização do vetor 'matriz'
    matriz = []

    # estrutura de repetição em que 'i' percorre o numero de linhas e adiciona um vetor dentro do vetor matriz (dando origem assim a uma matriz).
    # perceba que a variável 'N' não é utilizada para a leitura das colunas
    for i in range(M):
        # variável 'linha' lê cada linha digitada
        linha = [int(v) for v in input().split()]
        # método append adiciona o vetor salvo em 'linha' à matriz 'm'
        matriz.append(linha)

    # estrutura de repetição que percorrerá cada vetor dentro da matriz
    for i in matriz:
        # estrutura de repetição que percorrerá cada valor dentro do vetor
        for e in i:
            produtividade += e
    
    # estrutura de rapetição que dividirá a produtividade em sacas
    while (produtividade >= 60):
        saca += 1
        produtividade -= 60
    
    # saída imprime o número de sacas e a litragem restante
    print("{} saca(s) e {} litro(s)" .format(saca, produtividade))

exit(0)
