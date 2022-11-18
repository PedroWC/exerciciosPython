# -*- coding: utf-8 -*-
# Programa: monteCarlo.py
# Programador: Pedro Carvalhaes
# Data: 22/04/2020
# O Diálogo: Programa para calcular a área sob o gráfico de uma função f
# usando o método de Monte Carlo. O método de Monte Carlo consiste em
# lançar q dardos numa dada região e contar os que acertaram uma
# subregião. No nosso caso consideramos o retângulo com base [a, b]
# e altura m, onde f(x) <= m para todos x em [a, b]. Considere a
# área nesse retângulo delimitada pela curva da função f(x).
# O método consiste em contar o número total p que acertam a região
# que fique abaixo (incluindo a curva) da função y = f(x). Para um
# número grande de lançamentos, temos que a proporção p/q é
# aproximadamente igual a área sob a curva dividida pela área total
# do retângulo.
# Declaração das bibliotecas utilizadas
import random

# início

# le os valores da entrada
for A in range (1000):
   # le o valor do limite inferior do intervalo
   a = float(input("Entre com o valor de a: "))
   if a == 0:
      break
   
   # le o valor do limite superior do intervalo
   b = float(input("Entre com o valor de b: "))
   
   # le o valor máximo da função no intervalo
   m = float(input("Entre com o valor de m: "))
   
   # le o número de lançamentos do dardo
   n = int(input("Entre com o valor de n: "))
   
   # Calcula área sob a curva
   
   # Inicializa as variáveis
   area = 0.0
   hits = 0
   
   # Calcula o intervalo [a,b]
   x = b - a
   
   # Define uma semente
   random.seed(997)
   
   # Simula n lançamentos do dardo
   for i in range (n):
   # Passo 2.4.1. Calcule as coordenadas (x,y) para o dardo
      xlan = random.uniform(a, b)
      ylan = random.uniform(0, m)
   # Passo 2.4.2. Verifique a região que o dardo acertou
      if (ylan < (xlan * xlan + 1)):
         hits += 1
   # fim do for
   
   # Computa a área aproximada
   area = (x * m * hits) / n
   
   # Imprime o valor da área
   print("A área aproximada usando {0:d} lançamentos é {1:f}".format(n,area))
   
   # fim