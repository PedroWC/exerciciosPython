cc = 'FF'
entrada = input()
entrada = entrada.split(',')

saida = ''
cont = 1

for indice in range(len(entrada)):
    if( indice < (len(entrada) - 1)):
        if cont:
            if( entrada[indice] == entrada[indice + 1] ):
                saida += cc
                repet, cont = 2, 0

            saida += str(entrada[indice])

        else:
            if( entrada[indice] == entrada[indice + 1] ):
                repet += 1

            else:
                saida += str(repet)
                cont = 1
    elif not ( entrada[indice] == entrada[indice - 1] ):
        saida += str(entrada[indice])

print(saida)
