# -*- coding: utf-8 -*-
# Programa: charordem.py
# Programador:
# Data: 05/04/2011
# Este programa lê quatro caracteres letra1, letra2, letra3 e letra4 e
# verifica se elses são do alfabeto. Se os caracteres forem do alfabeto,
# o programa verifica se estão em ordem crescente. O programa
# imprime mensagens adequadas.

# início
# pré: letra1 letra2 letra3 letra4

# Passo 1.1. Leia quatro caracteres
letra = list(input())
e = letra.index(" ")
for i in range (e):
    letra.remove(" ")

# Passo 1.2. Inicialize algumas variáveis
count = 0
desordem = 0

# Passo 2.1. Verifique se algum dos caracteres são lestras do alfabeto
for i in letra:
    if(i.isalpha()) == True:
        count += 1

# Passo 2.2. Verifique se os caracteres estão em ordem crescente
max = len(letra)
for i in range (1, max, +1):
    if letra[i] < letra[i-1]:
        desordem = 1

# Passo 3. Imprima a mensagem correspondente
if count > 0:
    if desordem == 1:
        print('Os caracteres não estão em ordem crescente.')
    else:
        print('Os caracteres estão em ordem crescente.')
else:
    print('Pelo menos um dos caracteres não é do alfabeto.')
#print('{0:s}'.format(msg))
# pós: (letra1 < letra2 && letra2 < letra3 && letra3 < letra4) && os caracteres
#      estão em ordem crescente) || (Os caracteres nao estao em ordem crescente) 
# fim
exit(0)