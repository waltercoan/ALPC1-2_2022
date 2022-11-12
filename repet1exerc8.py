'''
Elaborar um programa que efetue a leitura de valores 
positivos inteiros até que um valor negativo seja 
informado. Ao final deve ser apresentados o maior 
e o menor número informado pelo usuário.
'''
omaior = 0
omenor = 0
contador = 0
while True:
    print("Digite um numero")
    n = int(input())
    if n < 0:
        break
    if n > omaior:
        omaior = n
    #nunca misturar a logica do maior e do menor
    if contador == 0:
        omenor = n
    if n < omenor:
        omenor = n
    contador = contador + 1
    
print("O maior e ", omaior)
print(f"O maior e {omaior}")
print("O menor e ", omenor)
print("ate logo e obrigado pelos peixes")
