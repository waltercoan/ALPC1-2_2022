#declaração de variaveis
valaumento = 0
print("Digite o valor do salario")
valsalario = float(input())

if valsalario <= 300:
    valaumento = (valsalario * 15) / 100
else:
    if valsalario > 300 and valsalario < 600:
        valaumento = (valsalario * 10) / 100
    else:
        if valsalario >= 600 and valsalario <= 900:
            valaumento = (valsalario * 5) / 100
        else:
            valaumento = (valsalario * 2) / 100
print("O valor do aumento e ", valaumento)
valnovosal = valsalario + valaumento
print("O valor do novo salario e ", valnovosal)
