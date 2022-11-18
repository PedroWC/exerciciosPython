#Lendo o número do usuário. Convertendo a string lida em inteiro
n = int(input("Digite um inteiro de três dígitos:"))



# descobrindo qual o dígito menos significativo
d3 = n%10

#atualizando o número a ser desmembrado
n = n // 10

# descobrindo qual o dígito do meio
d2 = n%10

#atualizando o número a ser desmembrado
n = n // 10


# descobrindo qual o dígito mais significativo
d1 = n%10


# Imprimindo os resultados
print("%d %d %d" %(d1, d2, d3))