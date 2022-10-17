print("Digite o valor da prestação")
valor = float(input())
print("Digite o perc da Taxa")
taxa = float(input())
print("Digite o tempo em dias de atraso")
tempoemdias = int(input())
prestacao = valor + (valor * (taxa / 100)) * tempoemdias
print("O valor da prestação e", prestacao)

