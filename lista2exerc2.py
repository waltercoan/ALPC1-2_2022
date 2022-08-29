#ENTRADAS
print("Digite a sua idade")
idade = int(input())
#PROCESSAMENTO
if idade > 0 and idade <= 20:
    #então
    print("Jovem")
#fimdoentao
else:
    #senão
    if idade > 20 and idade < 70:
        #entao
        print("Adulto")
    #fimentao
    else:
        if idade > 0:
            print("Idoso")
        else:
            print("Idade invalida")
    #fimsenao
#fimsenao

