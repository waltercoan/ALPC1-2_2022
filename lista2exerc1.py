#ENTRADAS
print("Digite um numero")
num1 = int(input())
print("Digite outro numero")
num2 = int(input())
#PROCESSAMENTO
if num1 == num2:
    #bloco sim
    print("São iguais")
    media = (num1 + num2) / 2
    print("A media e ", media)
#FIM bloco sim
else: 
    if num1 > num2:
        #bloco sim
        print("o maior e ", num1)
        print("O menor e ", num2)
    else:
        print("O maior e", num2)
        print("o menor e", num1)
#fim