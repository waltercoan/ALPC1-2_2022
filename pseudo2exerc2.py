print("Digite o valor médio de venda mensal")
valmedvenda = float(input())
print("Digite o preco atual")
precoatual = float(input())
if valmedvenda < 500 or precoatual < 30:
    valaumento = precoatual * 12 / 100
    print("O valor do aumento e ",valaumento)
    novopreco = precoatual + valaumento
else:
    if (valmedvenda >= 500 and valmedvenda < 1600) or \
        (precoatual>= 30 and precoatual < 80):
        valaumento = precoatual * 15 / 100
        print("O valor do aumento e ",valaumento)
        novopreco = precoatual + valaumento
    else:
        if valmedvenda >= 1600 or precoatual >= 80:
            valreducao = precoatual * 25 / 100
            print("O valor do desconto de ",valreducao)
            novopreco = precoatual - valreducao
print("Novo preco", novopreco)
