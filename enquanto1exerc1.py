"""
Faça um algoritmo que calcule a multiplicação de
 dois números inteiros sem utilizar o operador “*”. 
 Em vez disso, utilize apenas o operador de adição “+”. 
 Para implementar esse algoritmo, devemos lembrar que 
 qualquer multiplicação pode ser expressa por meio 
 de somas. Por exemplo, o resultado da expressão 6 * 3 é o mesmo que 6 + 6 + 6 ou 3 + 3 + 3 + 3 + 3 + 3. Ou seja, soma-se um elemento com ele próprio o número de vezes do segundo elemento.
"""
print("Digite o primeiro numero")
n1 = int(input())
print("Digite o segundo numero")
n2 = int(input())

soma = 0
for cont in range(n2):
    #print("rodando")
    soma = soma + n1
print(n1, "X", n2, " = ", soma)
