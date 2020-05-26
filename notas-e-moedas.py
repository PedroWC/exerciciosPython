#Codigo lê um número com duas casas decimais e salva na memoria A
A = float(input())

#Divisao das cedulas
_100 = int(A) / 100
N = int(A) % 100
_50 = N / 50
N = N % 50
_20 = N / 20
N = N % 20
_10 = N / 10
N = N % 10
_5 = N /5
N = N % 5
_2 = N / 2
N = N % 2
_1 = N / 1

#Para facilitar as contas, elimino os digitos antes da vírgula e obtenho somente os digitos das casas decimais salvos em S
DecimalTemp = A - int(A)
S = DecimalTemp * 100

#Divisão das moedas
_05 = S / 50
S = S % 50
_025 = S / 25
S = S % 25
_010 = S / 10
S = S % 10
_005 = S / 5
S = S % 5
_001 = S / 1
S = S % 1

#Pela precisão do python se tornar um obstaculo em nosso calculo,
#nessa condicional eu resolvo o problema da margem de erro das moedas de 1 centavo
if S > 0.5:
    _001 = _001 + 1

#Resultados
print("NOTAS:")
print("%d nota(s) de R$ 100.00" %_100)
print("%d nota(s) de R$ 50.00" %_50)
print("%d nota(s) de R$ 20.00" %_20)
print("%d nota(s) de R$ 10.00" %_10)
print("%d nota(s) de R$ 5.00" %_5)
print("%d nota(s) de R$ 2.00" %_2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %_1)
print("%d moeda(s) de R$ 0.50" %_05)
print("%d moeda(s) de R$ 0.25" %_025)
print("%d moeda(s) de R$ 0.10" %_010)
print("%d moeda(s) de R$ 0.05" %_005)
print("%d moeda(s) de R$ 0.01" %_001)

exit(0)