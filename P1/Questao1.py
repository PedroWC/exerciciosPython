#leitura dos valores da compra e pago pelo cliente, respectivamente
valor_compra = int(input())
valor_pago = int(input())

#Cálculo do troco
valor_troco = valor_pago - valor_compra

#Divisão das notas
_50 = valor_troco // 50
valor_troco = valor_troco % 50
_10 = valor_troco // 10
valor_troco = valor_troco % 10
_5 = valor_troco // 5
valor_troco = valor_troco % 5
_1 = valor_troco

#Impressão do resultado
print("Saída Correspondente:")
print("Notas de 1 = {}" .format(_1))
print("Notas de 5 = {}" .format(_5))
print("Notas de 10 = {}" .format(_10))
print("Notas de 50 = {}" .format(_50))

exit(0)