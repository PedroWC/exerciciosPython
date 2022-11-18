class Celula: #Criando a representação das células

    # Construtor
    def __init__(self, nome:str, idade:str, altura:str, ant:object = None):
        self.nome   = nome
        self.idade  = idade
        self.altura = altura
        self.ant    = ant

    #definido o formato de impressão da célula        
    def __str__(self) -> str:
        return 'Celula('+str(self.nome)+','+str(self.idade)+','+str(self.altura)+')'
        

#Criando uma célula e armazenando na variável n1
n1 = Celula(input(),input(),input())
print(n1)
#Criando uma célula e armazenando na variável n2 e apontando para n1
n2 = Celula(input(),input(),input(),n1)
print(n2)
#Criando uma célula e armazenando na variável n3 e apontando para n2
n3 = Celula(input(),input(),input(),n2)
print(n3)