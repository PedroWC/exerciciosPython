decimal = int(input("Insira um numero decimal inteiro:\n"))
i = 0
binar = []

#guardar numero na forma binarária invertida no vet "binar[]"
while decimal >= 1:
    binar.insert(i , int(decimal % 2))
    i += 1
    decimal //= 2

# a = auxiliar para contagem de memorias no vetor "binar[]"
a = i

print("\nO número em sua forma binarária é: \n")

#inverter vetor binar[]
binar.reverse()
#Impressão do numero binário
for i in range(a):
    print("{}" .format(binar[i]), end="")
else:
    print("\n")

exit(0)