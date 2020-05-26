# -*- coding: utf-8 -*-

dia1, hora1, minuto1, segundo1 = input().split()
dia1, hora1, minuto1, segundo1 = int(dia1), int(hora1), int(minuto1), int(segundo1)

dia2, hora2, minuto2, segundo2 = input().split()
dia2, hora2, minuto2, segundo2 = int(dia2), int(hora2), int(minuto2), int(segundo2)

resultDia = 0
resultHora = 0
resultMinuto = 0
resultSegundo = 0

#segundo
resultSegundo = segundo1 + segundo2

if resultSegundo >= 60:   #se ultrapassar 60 seg -> +1 min
    resultSegundo -= 60
    resultMinuto = 1

#minuto
resultMinuto += minuto1 + minuto2


if resultMinuto >= 60:   #se ultrapassar 60 min -> +1hora
    resultMinuto -= 60
    resultHora = 1

#hora
resultHora += hora1 + hora2

if resultHora >= 24:   #se ultrapassar 24 horas -> +1 dia
    resultHora -= 24
    resultDia = 1

#Dia
resultDia += dia1 + dia2


print("{0} {1} {2} {3}" .format(resultDia, resultHora, resultMinuto, resultSegundo))

exit(0)