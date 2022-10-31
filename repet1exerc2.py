'''
Elabore um programa que apresente no final o 
somatório dos valores pares existentes na faixa de 1 até 500.
'''
contador = 1
soma = 0
while contador <= 500:
    if contador % 2 == 0: # se contador resto da div por 2 igual zero
        print(contador, end=" ")
        soma = soma + contador
    contador += 1 #contador = contador + 1
print("A soma dos pares de 1 a 500 e ", soma)

################

contador = 0
soma = 0
while contador <= 500:
    if contador % 2 == 1:
        print(contador, end=" ")
        soma = soma + contador
    contador += 1 #contador = contador + 1
print("A soma dos pares de 1 a 500 e ", soma)