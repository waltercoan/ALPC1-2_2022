#ENTRADAS
#print() imprime na tela
print("Digite o numero total de paginas")
#input() le dados do usuario
#int() converte a entrada para numerico
numtotalpag = int(input())
print("Digite o numero de dias")
numdias = int(input())
#PROCESSAMENTO
numpagdia = numtotalpag/numdias
if numpagdia > 100: 
    #entao/SIM/Verdadeiro
    print("E impossível!!!!")
else:
    #senao/NAO/FALSO
    print("E possivel ler", numpagdia)