# Inicio
def conferenciaHexadecimal(digito):
    if digito == 10:
        return "A"
    if digito == 11:
        return "B"
    if digito == 12:
        return "C"
    if digito == 13:
        return "D"
    if digito == 14:
        return "E"
    if digito == 15:
        return "F"
    else:
        return digito

# Passo 1. Entrada de dados
decimal = int(input("Insira um número decimal inteiro:\n"))

# Inicialização do vetor binar[]
binar = []

#Passo 2.1. Guarde o numero na forma hexadecimal invertida no vet "binar[]"
while decimal >= 16:
    digito = conferenciaHexadecimal(decimal % 16)
    decimal //= 16
    binar.append(digito)
digito = conferenciaHexadecimal(decimal)
binar.append(digito)

# Passo 2.2. Inverta o vetor binar[]
binar.reverse()

# Passo 3. Imprima o numero na forma hexadecimal
print("\nO número em sua forma hexadecimal é: \n")

for i in binar:
    print(i, end="")

exit(0)