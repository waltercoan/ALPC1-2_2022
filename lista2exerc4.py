#entrada
print("Digite a velocidade")
velocidade = float(input())
#processamento
if velocidade <= 60:
    print("Não há multa")
else:
    if velocidade > 60 and velocidade <= 100:
        print("Multa de 60 UFIR")
    else:
        if velocidade > 100 and velocidade <= 160:
            print("Multa de 120 UFIR")
        else:
            print("Multa de 180 UFIR")
    
