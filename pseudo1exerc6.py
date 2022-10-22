from abc import abstractmethod


print("Digite o preco")
preco = float(input())

if preco <= 50:
    valau = preco * 5 / 100
#fim IF
else:
    if preco > 50 and preco <= 100:
        valau = preco * 10 /100
    #fim IF
    else:
        valau = preco * 15 / 100
    #fim else
#fimelse
print("O valor do aumento e ", valau)
novopreco = preco + valau
if novopreco <= 80:
    print("Barato")
#fim if
else:
    if novopreco > 80 and \
        novopreco <= 120:
        print("Normal")
    #fim IF
    else:
        if novopreco > 120 and \
            novopreco <= 200:
            print("Caro")
        #fim if
        else:
            print("Muito caro")
