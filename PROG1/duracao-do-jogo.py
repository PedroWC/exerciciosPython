hora_inicial = int(input("Digite o valor de hora do horario de início do processo:   "))
minuto_inicial = int(input("Digite o valor de minuto do horario de início do processo:   "))
segundo_inicial = int(input("Digite o valor de segundo do horario de início do processo:   "))

hora_final = int(input("Digite o valor de hora do horario de fim do processo:   "))
minuto_final = int(input("Digite o valor de minuto do horario de fim do processo:   "))
segundo_final = int(input("Digite o valor de segundo do horario de fim do processo:   "))

if (segundo_inicial > segundo_final):
    segundo_final = segundo_final + 60
    minuto_final = minuto_final - 1
duracao_segundo = segundo_final - segundo_inicial

if(minuto_inicial > minuto_final):
    minuto_final = minuto_final + 60
    hora_final = hora_final - 1
duracao_minuto = minuto_final - minuto_inicial

if (hora_final < hora_inicial):
    hora_final = hora_final + 24
duracao_hora = hora_final - hora_inicial

print("A duração do processo foi %d horas, %d minutos e %d segundos" %(duracao_hora, duracao_minuto, duracao_segundo))

exit(0)