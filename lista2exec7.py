'''
print("Digite a qtd de minutos")
qtdminutos = float(input())
print("Digite a origem")
print("-local")
print("-intermunicipal")
print("-interestadual")
origem = input()

if origem == "local":
    valortotal = qtdminutos * 0.02
    print("O valor total e ", valortotal)
else:
    if origem == "intermunicipal":
        valortotal = qtdminutos * 0.08
        print("O valor total e ", valortotal)
    else:
        valortotal = qtdminutos * 0.1
        print("O valor total e ", valortotal)

'''
print("Digite a qtd de minutos")
qtdminutos = float(input())
print("Digite a origem")
print("-local")
print("-intermunicipal")
print("-interestadual")
origem = input()

if origem == "local":
    valminuto = 0.02
else:
    if origem == "intermunicipal":
        valminuto = 0.08
    else:
        valminuto = 0.1

valortotal = qtdminutos * valminuto
print("O valor total e ", valortotal)


