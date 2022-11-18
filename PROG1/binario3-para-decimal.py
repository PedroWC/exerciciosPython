# -*- coding: utf-8 -*-
# Programa: convertedec.c
# Programador:Pedro Carvalhaes
# Data: 19/03/2020
# Este programa lê um número binário de até 3 dígitos e calcula, seu
# equivalente na base 10 e imprime o resultado.


# Passo 1. Leia um número binário de até três dígitos
binario = int(input())


# Passo 2. Converta o número para a base 10.
# descobrindo qual o dígito menos significativo
digito = binario % 10
decimal = digito * 1

#atualizando o número a ser desmembrado
aux = binario // 10

# descobrindo qual o dígito do meio
digito = aux % 10
decimal += digito * 2

#atualizando o número a ser desmembrado
aux = aux // 10

# descobrindo qual o dígito mais significativo
digito = aux % 10
decimal += digito * 4


# Passo 3. Imprima o número decimal correspondente
print('{0:d} (base 2) == {1:d} (base 10)'.format(binario, decimal))

# pós: decimal=(((binario/10)/10)%10)*2^1+((binari/10%10)*2^1+(binario%10)*2^0