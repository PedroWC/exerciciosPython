# -*- coding: utf-8 -*-

# Funções
#uma função da linguagem Python é um trecho de código que
#pode receber um ou mais valores de entrada armazenados em
#variáveis, chamados de parâmetros (de entrada), que realiza
#algum processamento específico e que pode devolver um ou mais
#valores de saída

##########EXEMPLO 1
#funções nativas (built-in)
lista = [4, 3, 2, 5, 6, 4, 33, 4, 2]
#função max que, dada uma lista de entrada retorna
#o maior elemento da lista
maximo = max(lista)

#função que imprime na tela o conteúdo da
#variável passada como parâmentro de entrada
print(maximo)




##########EXEMPLO 2
#funções disponíveis em módulos/bibliotecas
import math

n = int(input("Digite o inteiro para o cálculo da raiz quadrada: "))
#chama a função sqrt que está disponível na biblioteca math
raiz = math.sqrt(n)
print(raiz)






##########EXEMPLO 3
#criando nossas próprias funções

###### MÉDIA 1
###### leia dois inteiros e retorne a média destes
#definição da função média
def media(a, b):
  return (a+b)/2
  

#entrada
n1 = int(input())
n2 = int(input())

#processamento
#chamada à função média que retorna
#a média calculada para os valores
#de entrada informados como parâmetros para
#a função
m = media(n1, n2)

#saída
print(m)





##########EXEMPLO 4
#criando nossas próprias funções

###### MÉDIA 2
###### leia dois inteiros e retorne a média destes
#definição da função média
def media(n1, n2):
  #note que as variáveis n1 e n2 são locais, ou seja, pertencem
  #apenas à esta função. Estas variáveis receberam uma cópia
  #dos valores das variáveis vindas da função principal
  resultado =  (n1+n2)/2
  n1 = -100 #alterando o valor da variável local
  n2 = 500 #alterando o valor da variável local
  return resultado
  

#entrada
n1 = int(input())
n2 = int(input())

#processamento
#chamada à função média que retorna
#a média calculada para os valores
#de entrada informados como parâmetros para
#a função
m = media(n1, n2)

#saída
print("A média entre os valores %d e %d é %0.2f" %(n1, n2, c))





##########EXEMPLO 5
#criando nossas próprias funções

###### Modificando listas
#definir as funções
def Imprime(Lista):
  print("A lista de inteiros armazendos é: ")
  for i in range(len(Lista)):
    print("%d", end=' ')
  print()


def Modifica(L, i):
  #troca o valor do primeiro elemento por zero
  L[i] = 0
  i = -7
  
#corpo principal (main)

lista = []
# entrada
lista = list(map(int,  input().split()))

#Imprime a lista lida
Imprime(lista)

#Modifica a lista lida
i = 3
Modifica(lista, i)
print(i)
#


#Imprime a lista 
Imprime(lista)




















# Exemplo 6
#Funcao que modifica uma lista
def remove_min(l):
  menor    = l[0]
  i_menor = 0
  for i in range(len(l)):
    if(l[i] < menor):
      menor = l[i]#atualiza o menor
      i_menor = i#atualiza o indice onde o menor elemento foi encontrado
      
    #agora que encontramos o menor elemento,
    #este deve ser removido da lista (este código irá sobreescrever o menor elemento)
  for i in range(i_menor, len(l)-1, 1):
    l[i] = l[i+1]
  l.pop()#exclui o último elemento da lista


lista = []
lista = list(map(int, input("Digite a lista de elementos:").split()))
print(lista)
remove_min(lista)
print(lista)









###### vamos implementar a nossa função para determinar
###### o maior elemento de uma lista
