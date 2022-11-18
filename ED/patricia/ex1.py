#Criar a estrutura de uma patricia para armazenar as vogais
class no:
    #Inicializando os campos do nó
    def __init__(self,chave=None):
        self.chave    = chave
        self.marcador = 0
        self.filhos   = {
            'a': None,
            'e': None,
            'i': None,
            'o': None,
            'u': None
        }

    #Imprimindo os campos do nó    
    def __str__(self):    
        return 'No('+str(self.chave)+')'

    def inserir(self, palavra: str):
        primeira_letra = palavra[0]
        n = no(palavra)
        self.filhos.update({primeira_letra : n})

        return self.filhos[primeira_letra]

raiz = no()
linha1 = raiz.inserir('al')
linha2 = linha1.inserir('egria')
linha2 = linha1.inserir('ugar')