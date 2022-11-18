
class celula:
    def __init__(self):
        self.raiz = None
        self.fe   = None
        self.fd   = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def buscaPai(self, valor):
        aux1 = self.raiz
        aux2 = None

        while (aux1 != None):
            aux2 = aux1
            aux1 = aux1.fe if (valor < aux1.valor) else aux1.fd

        return aux2

    def insercao(self, valor):
        novo = celula(valor)
        self.raiz = novo if (self.raiz == None) else 


class ABB:
    def __init__(self, raiz):
        self.raiz = raiz
