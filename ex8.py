# -*- coding: utf-8 -*-
# Programa: somaGraus.py
# Programador: Pedro Carvalhaes
# Data: 19/03/2020

###   LEITURA DE DADOS   ###
g1, m1, s1 = input().split()
g1, m1, s1 = int(g1), int(m1), int(s1)
g2, m2, s2 = input().split()
g2, m2, s2 = int(g2), int(m2), int(s2)

###   CÁLCULO DE DADOS   ###

#segundos
somaS = s1 + s2

#minutos
somaM = m1 + m2
if somaS >= 60:
    somaM += 1
    somaS -= 60

#graus
somaG = g1 + g2
if somaM >= 60:
    somaG += 1
    somaM -= 60

#circulo
if somaG >= 360:
    somaG -= 360

###   IMPRESSÃO DOS DADOS   ###

print("{0:3d} Graus {1:2d} Minutos {2:2d} Segundos +" .format(g1, m1, s1))
print("{0:3d} Graus {1:2d} Minutos {2:2d} Segundos =" .format(g2, m2, s2))
print("{0:3d} Graus {1:2d} Minutos {2:2d} Segundos" .format(somaG, somaM, somaS))

exit(0)