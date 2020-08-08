# entrada da quantidade de testes
quantidade = int(input(''))

# variável e tomará como valores 0 até (quantidade - 1)
for e in range(quantidade):

    # entrada do texto codificado
    texto = input('')

    # entrada da quantidade de posições que cada letra foi deslocada para a direita
    quantidade = int(input(''))

    # inicialização da variável que receberá o texto decodificado
    texto_decodificado = ''

    # estrutura de repetição que percorrerá cada letra do texto codificado
    for e in texto:

        # variável 'posicao' recebe posição da letra guardada em 'e' deslocada
        posicao = ord(e) - quantidade

        # filtro para ordenar as letras em seu devido lugar na variável do texto decodificado
        if(posicao >= 65):
            texto_decodificado += chr(ord(e) - quantidade)
        else:
            texto_decodificado += chr(91 - (65-posicao))
            
    # saída com o texto ja decodificado
    print(texto_decodificado)

exit(0)