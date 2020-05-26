# -*- coding: utf-8 -*-
# Programa: charordem.py
# Programador:
# Data: 05/04/2011
# Este programa lê quatro caracteres letra1, letra2, letra3 e letra4 e
# verifica se elses são do alfabeto. Se os caracteres forem do alfabeto,
# o programa verifica se estão em ordem crescente. O programa
# imprime mensagens adequadas.

# Inicio
count = 0

# Passo 1.1. Leia quatro caracteres
letra = list(input())
e = letra.count(" ")
for i in range (e):
    letra.remove(" ")

# Passo 2.1. Verifique se algum dos caracteres são lestras do alfabeto
for i in letra:
    if(i.isalpha()) == True:
        count += 1

# Passo 2.2. Verifique se os caracteres estão em ordem crescente
if count != 0:
    if letra.sort() == letra:
        print('Os caracteres estão em ordem crescente.')
    else:
        print('Os caracteres não estão em ordem crescente.')
else:
    print('Pelo menos um dos caracteres não é do alfabeto.')

exit(0)