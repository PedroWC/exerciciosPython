codigo1, num1, valor1 = input().split()
codigo1, num1, valor1 = int(), int(num1), float(valor1)

codigo2, num2, valor2 = input().split()
codigo2, num2, valor2 = int(), int(num2), float(valor2)


total = (valor1 * num1) + (valor2 * num2)

print("VALOR A PAGAR: R$ %.2f" %total)

exit(0)