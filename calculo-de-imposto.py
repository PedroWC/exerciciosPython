salarioanual = float(input("Digite sua renda anual a seguir:   "))

renda = salarioanual / 12

if renda < 1434.6:
    print("Isento de taxa")

elif renda >= 1434.60 and renda <= 2150:
    imposto = renda * 0.078
    print("Valor do imposto = R$%.2f" %(imposto))

elif renda > 2150 and renda <= 2866.70:
    imposto = renda * 0.15
    print("Valor do imposto = R$%.2f" %(imposto))

elif renda > 2866.70 and renda <= 3582:
    imposto = renda * 0.225
    print("Valor do imposto = R$%.2f" %(imposto))

else:
    imposto = renda * 0.275
    print("Valor do imposto = R$%.2f" %(imposto))

exit(0)