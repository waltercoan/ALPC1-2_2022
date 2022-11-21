"""
Faça um algoritmo que calcule a 
soma de todos os números ímpares 
dentro de uma faixa de valores 
determinada pelo usuário. Um número 
é ímpar quando sua divisão por 2 
não é exata, ou seja, o resto resultante
da divisão inteira pelo número 2 tem 
valor 1. Utilize a palavra resto como
operador que calcula o resto da 
divisão de um numero por outro.
"""
print("Digite o numero inicial")
ini = int(input())
print("Digite o numero final")
fim = int(input())

soma = 0
for cont in range(ini,fim+1):
    print(cont, end=" ")
    if cont % 2 == 1:
        soma += cont
print("A soma dos impares e", soma)
