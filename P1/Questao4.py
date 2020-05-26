# Leitura da quantidade de dias
dias = int(input())

# Inicialização das variáveis
anos = 0
meses = 0

# Validação dos dados
## Divisão por anos
if dias >= 360:
    anos += dias // 360
    dias %= 360

## Divisão por meses
if dias >= 30:
    meses += dias // 30
    dias %= 30

## O que restar ja esta dividido em dias

# Impressão dos anos, meses e dias
print("{} anos\n{} meses\n{} dias" .format(anos, meses, dias))

exit(0)