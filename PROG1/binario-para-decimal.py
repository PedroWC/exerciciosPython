# -*- coding: utf-8 -*-
# Programa: binario-para-decimal.py
# Programador:Pedro Carvalhaes
# Data: 29/04/2020
# Este programa lê um número binário de n dígitos, calcula seu
# equivalente na base 10 e imprime o resultado.

# -> Função utilizada para obter um numero em uma determinada 'posição' de
# uma 'lista' e transformalo em inteiro
def dig(lista, posicao):
    aux = lista[posicao]
    aux = int(aux)

    return aux


# Passo 1. Leia um número binário
binario = list(input("Digite o número binário:\n"))


# -> lengh receberá o numero  de espaços que a lista contém mais um
# para orientar o loop for
# -> Digito recebera o mesmo numero de espaços para orientar o
# espaço do vetor a ser utilizado dentro do loop
# -> Inicialização do decimal
lengh = len(binario)
digito = len(binario) - 1
decimal = 0

# Passo 2. Use um loop para converter cada digito do binario
for i in range (lengh):
    decimal += dig(binario, digito) * (2**i)
    digito -= 1

# Passo 3. Imprima o número decimal correspondente
print('== {0:d} (base 10)'.format(decimal))

exit(0)