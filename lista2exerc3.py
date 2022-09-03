qtdtotcol = 0
#print - mostra em tela mensagem
print("Digite a qtd de colestrol")
#input - le dados digitados
#int() - converte em inteiro
#float() - converte em decimal 
qtdtotcol = float(input())
if qtdtotcol <= 130:
    #entao - sim - verdadeiro
    print("Tudo bem")
else:
    #senao - nao - falso
    perccol = (qtdtotcol * 100) / 130
    print("Colesterol acima do normal")
    print(perccol)
