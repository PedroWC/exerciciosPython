#Criar a estrutura de uma trie para armazenar as vogais
class No:
    #Inicializando os campos do nó
    def __init__(self, letra=None):
        self.letra  = letra
        self.cor    = 0
        self.filhos = {
            'a': None,
            'e': None,
            'i': None,
            'o': None,
            'u': None
        }
        
    def inserir(self, letra):
        self.filhos[letra] = No(letra)

        return self.filhos[letra]
        

    #Imprimindo os campos do nó    
    def __str__(self):    
        return 'No('+str(self.letra)+')'

raiz        = No()
atual       = raiz.inserir('a')
atual       = atual.inserir('e')
atual       = atual.inserir('i')
atual.cor   = 1