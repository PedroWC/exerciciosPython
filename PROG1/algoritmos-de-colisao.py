#Leitura de dados
#Quadrado 1
#Ponto inferior esquerdo
x_inf_1 = int(input("Digite o valor de x do canto inferior esquerdo do primeiro quadrado:   "))
fx_inf_1 = int(input("digite o valor de f(x) do canto inferior esquerdo do primeiro quadrado:   "))
#Ponto superior direito
x_sup_1 = int(input("Digite o valor de x do canto superior direito do primeiro quadrado:   "))
fx_sup_1 = int(input("digite o valor de f(x) do canto superior direito do primeiro quadrado:   "))

#Quadrado 2
#Ponto inferior esquerdo
x_inf_2 = int(input("Digite o valor de x do canto inferior esquerdo do segundo quadrado:   "))
fx_inf_2 = int(input("digite o valor de f(x) do canto inferior esquerdo do segundo quadrado:   "))
#Ponto superior direito
x_sup_2 = int(input("Digite o valor de x do canto superior direito do segundo quadrado:   "))
fx_sup_2 = int(input("digite o valor de f(x) do canto superior direito do segundo quadrado:   "))

#Q1 está a direita ou a cima de Q2 (e vice versa)
if (x_inf_1 > x_sup_2) or (fx_inf_1 > fx_sup_2) or (x_inf_2 > x_sup_1) or (fx_inf_2 > fx_sup_1): 
    print("Os quadrados não se colidem")

#Q1 está a baixo ou a esquerda de Q2 (e vice versa)
else:
    if (fx_sup_1 < fx_inf_2) or (x_sup_1 < x_inf_2) or (fx_sup_2 < fx_inf_1) or (x_sup_2 < x_inf_1): 
        print("Os quadrados não se colidem")


    else:
        #Q1 está dentro de Q2 (e vice versa)
        if ((fx_inf_2 > fx_inf_1) and (fx_sup_2 < fx_sup_1)) or ((fx_inf_1 > fx_inf_2) and (fx_sup_1 < fx_sup_2)):
            print("Os quadrados não se colidem")

        #Nenhuma das proposições são verdadeiras
        else:
            print("Os quadrados se colidem")
exit(0)