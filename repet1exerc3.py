'''
REPETIÇÃO3) Faça um programa que leia um
valor N inteiro e positivo. Calcule e
 mostre o valor de E, conforme a fórmula a seguir:
E = 1 + 1/(1!) + 1/(2!) + 1/(3!) + ... + 1/(N!)
E = 1 + 1/(1!) + 1/(2!) + 1/(3!)
E = 1 + 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + 1/(5!)
'''

print("Digite o valor de N")
n = int(input())

contador = 1
E = 1
while contador <= n:
    #print("Rodando")
    fat = contador
    print(fat,"!=",end=" ")
    result = 1
    while fat > 0:
        print("\t", fat)
        result = result * fat
        fat = fat - 1
    print(result)
    E = E + (1/result)
    contador = contador + 1
print("E=", E)