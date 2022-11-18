#Classe para implementaraTabela de Rehash Linear
class TabelaHash:
    def __init__(self, M, codigo = -1):
        self.codigo = codigo
        self.tabela = [self.codigo] * M
        self.M      = M

   #Função para mapear a chave em uma posição
    def hashFun(self, chave, i = 0) -> int:
        pos = (chave + i) % self.M

        return pos if self.tabela[pos] == self.codigo else self.hashFun(chave, i + 1)

    def inserir(self, chave) -> None:
        pos = self.hashFun(chave)
        
        self.tabela[pos] = chave
    
t = TabelaHash(7)
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
print(t.tabela)