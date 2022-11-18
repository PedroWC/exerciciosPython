
class Celula: #Criando a representação das células

    # Construtor
    def __init__(self, nome:str, idade:int, altura:float):
        self.nome   = nome
        self.idade  = idade
        self.altura = altura
        self._prox  = None
    
    @property
    def prox(self):
        return self._prox

    @prox.setter
    def prox(self, prox):
        self._prox = prox

    #definido o formato de impressão da célula        
    def __str__(self) -> str:

        r = str(self.nome) + '\n' + str(self.idade) + '\n' + str(self.altura)

        return r + '\n' + self.prox.__str__() if(self.prox != None) else r

# Criando *uma célula* e armazenando na variável n1
n1 = Celula(input(),int(input()),float(input()))
# Criando *uma célula* e armazenando na variável n2
n2 = Celula(input(),int(input()),float(input()))
# Criando *uma célula* e armazenando na variável n3
n3 = Celula(input(),int(input()),float(input()))
# apontando n1 para n2
n1.prox = n2
# apontando n2 para n3
n2.prox = n3