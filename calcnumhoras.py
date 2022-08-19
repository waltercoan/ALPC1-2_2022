#1)	Faça um algoritmo que solicite o número 
# de horas que um trabalhador realiza por dia, 
# solicite o número de dias trabalhados em um 
# mês e apresente o número total de horas 
# trabalhadas no mês.

print("Digite o número de horas trabalhadas dia")
#int() converte texto em numero
numhorasdia = int(input())
print("Digite o número de dias trabalhados")
numdiastrab = int(input())
numtothoras = numhorasdia * numdiastrab
print("O número total de horas e ", numtothoras)