#Classe para implementaraTabela de Espalhamento(Hashing)
class TabelaHash:
    def __init__(self, M, codigo = -1):
        self.codigo = codigo
        self.tabela = [self.codigo]*M
        self.M      = M

   #Função para mapear a chave em uma posição
    def hashFun(self, chave):
        pos = chave % self.M

        return pos

    def inserir(self,chave):
        pos = self.hashFun(chave)

        if self.tabela[pos] == self.codigo:
           self.tabela[pos] = chave
    
t = TabelaHash(7)
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
print(t.tabela)