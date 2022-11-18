# Leitura da hora inicial do evento
hora, minuto, segundo = input().split(":")
hora, minuto, segundo = int(hora), int(minuto), int(segundo)

# leitura da duração total do evento
duracao = int(input())

# Atualização da hora e minuto inicial para final do evento
minuto += duracao
if minuto >= 60:
    hora += minuto // 60
    minuto %= 60
if hora >= 24:
    dia = hora // 24
    hora %= 24
else:
    dia = 0

# Impressão do horário final
if dia > 0:
    print("{}:{}:{}:{}" .format(dia, hora, minuto, segundo))
else:
    print("{}:{}:{}" .format(hora, minuto, segundo))

exit(0)