'''
Faça um programa que apresente no final o somatório 
dos números de 1 até 100.
'''

contador = 1
soma = 0
while contador <= 100:
    print(contador,end=" ")
    soma = soma + contador
    contador = contador + 1
print("A soma total de 1 ate 100 e ", soma)