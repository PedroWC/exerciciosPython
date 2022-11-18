populacao = float(input("Digite o tamanho populacional: "))
erro = int(input("Digite o erro amostral: "))

n0 = 1 / (erro/100) ** 2

tamanho_amostral = (n0 * populacao) / (n0 + populacao)

print("\nO tamanho amostral com {0:}% de erro para uma população de {1:.2f} é {2:.2f}" .format(erro, populacao, tamanho_amostral))

exit(0)