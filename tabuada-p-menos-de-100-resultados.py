n = int(input("Tabuada de qual numero você deseja?\n"))
quantidadeDeLinhas = int(input("Você deseja a tabuada do {} até qual número?\n" .format(n)))

print()

print("Tabuada do {}\n" .format(n))
quantidadeDeColunas = (quantidadeDeLinhas // 10)
if quantidadeDeLinhas % 10 != 0:
    quantidadeDeColunas += 1

    for i in range (1, 11):
        for a in range (0, quantidadeDeColunas - 1):
            resultado = n * ((a*10) + i)
            print("{0:2d} X {1:2d} = {2:2d}" .format(n, (a*10)+i, resultado), end="\t")
        if i <= quantidadeDeLinhas % 10:
            resultado =  n * (((quantidadeDeColunas-1)*10)+i)
            print("{0:2d} X {1:2d} = {2:2d}" .format(n, ((quantidadeDeColunas-1)*10)+i, resultado), end="\t")
        print("\n")

else:
    for i in range (1, 11):
        for a in range (quantidadeDeColunas):
            resultado = n * ((a*10) + i)
            print("{0:2d} X {1:2d} = {2:2d}" .format(n, (a*10)+i, resultado), end="\t")
        print("\n")

input("Pressione ENTER para continuar")

exit (0)