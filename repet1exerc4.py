'''
REPETIÇÃO4) Faça um programa que leia um número N 
que indica quantos valores inteiros e positivos devem ser 
lidos a seguir. 
Para cada número lido, mostre 
o valor lido e o fatorial  desse valor.
'''

print("Digite o valor de N")
n = int(input())

contador = 0
while contador < n:
    print("Digite o fatorial desejado")
    fat = int(input())
    print(f"{fat}!", end=" ")
    result = 1
    while fat > 0:
        #print("\t", fat)
        result *= fat
        #result = result * fat
        fat -= 1
    print(f" = {result}")
    contador += 1
    #contador = contador + 1