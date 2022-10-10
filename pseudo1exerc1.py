'''
Elaborar um programa que efetue o cálculo do 
valor da conversão em real (R$) de um valor 
lido em tela em dólar (US$). O programa deverá 
solicitar o valor da cotação do dólar.
ENTRADA
- valdolar
- valcotac
PROCESSAMENTO
valreais = valdolar * valcotac
SAIDA
- valreais
'''
#ENTRADAS
print("Digite o valor em dolar")
valdolar = float(input())
print("Digite o valor da cotacao")
valcotac = float(input())
#PROCESSAMENTO
valreais = valdolar * valcotac
#SAIDA
print("O valor em reais e ", valreais)
