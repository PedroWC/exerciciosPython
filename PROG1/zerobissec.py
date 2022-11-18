# -*- coding: utf-8 -*-
# Programa: zerobissec.py
# Programador: Pedro Carvalhaes
# Data: 22/04/2020
# O Diálogo: Programa para calcular os zeros de uma dada função 
# f de x = a até x = b usando o método da bisseção, o programa usa
# funções para ler os valores de a e b, para calcular os zeros e
# para imprimir os resultados. 
# É assumido que f(a) * f(b) < 0.0
# Declaração das bibliotecas utilizadas
import math

# início 

# pré: UmDouble1 UmDouble2

# Passo 1.1. Leia o valor do limite inferior
print('Entre com o valor de a: ')

# Passo 1.2. Leia o valor do limite superior
print('Entre com o valor de b: ')

# Passo 1.3. Leia o valor de epsilon
print('Entre com o valor de epsilon: ')

# Passo 2. Calcule um zero da função
# Passo 2.1. Incialize os extremos do intervalo

# Passo 2.2. Enquanto o intervalo for maior que epsilon e não achou raiz faça
while math.fabs(x1 - x2)> epsilon:
# Passo 2.2.1 Inicialize o valor da função nos extremos do intervalo 


# Passo 2.2.2. Calcule o valor da função no ponto médio do intervalo


# Passo 2.2.3. Verifique onde a função troca de sinal ou é um zero



   # fim if
# fim while
# Passo 3. Atribua o valor da raiz
raiz = m
# Passo 4. Imprima o zero da função
#   print('Um zero da função f(x) = xsen(x) - cos(x) no intervalo [{0:f},{1:f}] é {2:f}'.format(a, b, raiz))
print('{0:f}'.format(raiz))

# pós: raiz && f(raiz) == 0.0 
# fim
