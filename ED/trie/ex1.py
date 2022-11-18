#Criar a estrutura de uma trie para armazenar as vogais
class no:
    #Inicializando os campos do nó
    def __init__(self,letra=None):
        self.letra  = letra
        self.cor    = 0
        self.filhos = {
            'a': None,
            'e': None,
            'i': None,
            'o': None,
            'u': None
        }

    #Imprimindo os campos do nó    
    def __str__(self):    
        return 'No('+str(self.letra)+')'

raiz = no()
print(raiz.letra)
print(len(raiz.filhos))