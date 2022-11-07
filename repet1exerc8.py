'''
Elaborar um programa que efetue a leitura de valores 
positivos inteiros até que um valor negativo seja 
informado. Ao final deve ser apresentados o maior 
e o menor número informado pelo usuário.
'''
omaior = 0 
while True:
    print("Digite um numero")
    n = int(input())
    if n > omaior:
        omaior = n
    if n < 0:
        break
print("O maior e ", omaior)
print("ate logo e obrigado pelos peixes")
