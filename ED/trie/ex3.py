class No:

    #Inicializando os campos do nó
    def __init__(self, letra=None):
        
        self.letra  = letra
        self.fim    = 0
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
    
def inserir(chave: str, atual):
    
    for c in chave:
        atual = atual.inserir(c)

    atual.fim = 1

	
def busca(chave,atual):
    for c in chave:
        atual = atual.filhos[c]
        
        if(atual == None):
            break

    if(atual != None and atual.fim == 1):
        print('chave {%s} inserida!'%(chave))
    else:
        print('chave {%s} não foi inserida!'%(chave))

    return atual

#Main
raiz  = No()
chave = input()
inserir(chave, raiz)
busca(chave, raiz)