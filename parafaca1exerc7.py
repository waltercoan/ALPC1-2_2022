somapontuacao = 0
qtdcanal4=0
qtdcanal5=0
qtdcanal7=0
qtdcanal12=0
for familia in range(10):
    print("Familia: ", familia+1)
    print("Digite o canal mais assistido")
    canal = int(input())
    if canal == 4:
        qtdcanal4 +=1
    if canal == 5:
        qtdcanal5 +=1
    if canal == 7:
        qtdcanal7 +=1
    if canal == 12:
        qtdcanal12 += 1
    print("Digite qtd de pessoas")
    qtdpessoas = int(input())
    somaidades = 0
    for umapessoa in range(qtdpessoas):
        print("Pessoa:> ", umapessoa+1)
        print("Digite a idade")
        idade = int(input())
        somaidades = somaidades + idade
    print("Digite a regiao")
    regiao = input()

    media = somaidades / qtdpessoas
    print("A media das idades e ", media)
    pontuacao = 0
    if media <= 30:
        if regiao == "n" or regiao == "l":
            pontuacao = 20
        else:
            pontuacao = 35
    else:
        if media > 30 and media <= 50:
            if regiao == 'n':
                pontuacao = 40
            else:
                if regiao == 's':
                    pontuacao = 50
                else:
                    pontuacao = 60
        else:
            pontuacao = 30
    print("A pontuacao da familia e ", pontuacao)
    somapontuacao = somapontuacao + pontuacao

mediafamilia = somapontuacao / 10
print("A media de pontuacao da familia e ", mediafamilia)
'''
P     %
10   100
q4    P
10 * P = q4 * 100
P = (q4 * 100) / 10
'''
perccanal4 = qtdcanal4 * 100 / 10
print("O perc do canal 4 e ", perccanal4)
perccanal5 = qtdcanal5 * 100 / 10
print("O perc do canal 5 e ", perccanal5)
perccanal7 = qtdcanal7 * 100 / 10
print("O perc do canal 7 e ", perccanal7)
perccanal12 = qtdcanal12 * 100 / 10
print("O perc do canal 12 e ", perccanal12)

