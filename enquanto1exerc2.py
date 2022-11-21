'''
Faça um algoritmo que leia um número 
inteiro e calcule o seu fatorial. 
Se o número for negativo, informe 
que o valor é inválido. Sabemos 
que o fatorial de um número n, 
representado por n!, é dado por:
n * (n-1) * (n-2) * ... * 1, para n > 0 e n! = 1 para n = 0

'''
#print("Digite o numero do fatorial")
#fat = int(input())

resul = 1
for cont in range(fat,0,-1):
    #print(cont)
    resul = resul * cont
print(fat,"!=",resul)