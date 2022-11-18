n = int(input("Tabuada de qual numero você deseja?\n"))
quantidadeDeLinhas = int(input("Você deseja a tabuada do {} até qual número?\n" .format(n)))

#zerar memorias
quantidadeDeColunas = 0
blocos = 0

print() #pular uma linha

print("Tabuada do {}\n" .format(n))

###   CALCULAR NÚMERO DE BLOCOS   #########################################################
blocos = quantidadeDeLinhas // 100
###########################################################################################

###   IMPRESSÃO DOS BLOCOS DE 100 #########################################################
if quantidadeDeLinhas % 100 != 0: # SE A QUANTIDADE DE BLOCOS NÃO FOR MULTIPLA DE 100...................................
    blocos += 1

    for b in range (blocos - 1):
        for i in range (1, 11): #repetição das linhas
                for a in range (10): #repetição das colunas
                    A = (b * 100) + a * 10 + i
                    resultado = n * A
                    print("{0:2d} X {1:2d} = {2:2d}" .format(n, A, resultado), end="\t")
                print("\n")
        print("\n")

else: # SE A QUANTIDADE DE BLOCOS FOR MULTIPLA DE 100...................................................................
    for b in range (blocos):
        for i in range (1, 11): #repetição das linhas
                for a in range (10): #repetição das colunas
                    A = (b * 100) + a * 10 + i
                    resultado = n * A
                    print("{0:2d} X {1:2d} = {2:2d}" .format(n, A, resultado), end="\t")
                print("\n")
        print("\n")

###########################################################################################



### IMPRESSÃO DA SOBRA DOS BLOCOS DE 100 ##################################################

multiplicador = quantidadeDeLinhas // 100 # MULTIPLICADOR TEM A FUNÇÃO DE 
multiplicador *= 100 ###################### COLOCAR O ALGARISMO DA CENTENA

quantidadeDeLinhas %= 100 # AJUSTE PARA IMPRESSÃO APENAS DA SOBRA DOS BLOCOS DE 100
quantidadeDeColunas = quantidadeDeLinhas // 10

if quantidadeDeLinhas % 10 != 0: #SE A QUANTIDADE DE LINHAS FOREM MULTIPLAS DE 10.......................................
    quantidadeDeColunas += 1

    for i in range (1, 11): #repetição das linhas
        for a in range (0, quantidadeDeColunas - 1): #repetição das colunas
            A = a * 10 + multiplicador # ALGARISMOS DA DEZENA E CENTENA
            resultado = n * (A + i)
            print("{0:2d} X {1:3d} = {2:4d}" .format(n, A+i, resultado), end="\t")

        if i <= quantidadeDeLinhas % 10: # ÚLTIMA COLUNA DA LINHA
            A = (quantidadeDeColunas - 1) * 10 + multiplicador # ALGARISMOS DA DEZENA E CENTENA
            resultado =  n * (A + i)
            print("{0:2d} X {1:3d} = {2:4d}" .format(n, A+i, resultado), end="\t")
        print("\n")

else: #SE A QUANTIDADE DE LINHAS NÃO FOREM MULTIPLAS DE 10..............................................................

    for i in range (1, 11): #repetição das linhas
        for a in range (quantidadeDeColunas): #repetição das colunas
            A = a * 10 + multiplicador # ALGARISMOS DA DEZENA E CENTENA
            resultado = n * (A + i)
            print("{0:2d} X {1:3d} = {2:4d}" .format(n, A+i, resultado), end="\t")
        print("\n")
###########################################################################################

input("Pressione ENTER para continuar")

exit (0)