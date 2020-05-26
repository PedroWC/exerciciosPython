#Codigo lê um número inteiro e salva na memoria A
A = int(input())

#Divisao das cedulas
_100 = A / 100
N = A % 100
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

#Resultados
print("%d" %A)
print("%d nota(s) de R$ 100.00" %_100)
print("%d nota(s) de R$ 50.00" %_50)
print("%d nota(s) de R$ 20.00" %_20)
print("%d nota(s) de R$ 10.00" %_10)
print("%d nota(s) de R$ 5.00" %_5)
print("%d nota(s) de R$ 2.00" %_2)
print("%d nota(s) de R$ 1,00" %N)

exit(0)