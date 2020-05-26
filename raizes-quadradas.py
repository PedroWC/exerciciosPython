# Programador: Pedro Carvalhaes
# data 27/04/2020
# Este programa calcula as raízes reais da equação do raiz2undo 
# grau a*x^2 + b*x + c = 0 dado os coeficientes a, b e c
# declaração dos módulos utilizados
import math

# auxiliar serve para repetir o programa ate o usuário digitar "0"
aux = 1

while aux != 0:
    # Passo 1. Leia os Coeficientes
    a = float(input("Digite o valor de a:   "))
    b = float(input("Digite o valor de b:   "))
    c = float(input("Digite o valor de c:   "))
    # Passo 2. Calcule as raízes reais
    # Passo 2.1 Calcule a valor de Delta
    delta = b * b - 4 * a * c
    # Passo 2.2 Calcule as raízes (se existirem) e imprima os resultados
    if delta >= 0:
        delta = math.sqrt(delta)
        raiz1 = ((-b - delta) / (2 * a))
        raiz2 = ((delta - b) / (2 * a))
        print('As raízes são {0:.2f} e {1:.2f}\n'.format(raiz1, raiz2))
    else:
       print('A equação não possui raízes reais')
    
    # input para o usuario escolher repetir o programa ou não
    aux = int(input("Digite '1' para repetir o programa ou '0' para sair\n"))
else:
    exit(0)