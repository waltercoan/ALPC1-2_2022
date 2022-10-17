peso = 0
print("Digite a altura")
altura = float(input())
print("Digite o sexo (masculino/feminino)")
sexo = input()
if sexo == "Masculino" or sexo == "masculino":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7
print("O peso é: ", peso)
