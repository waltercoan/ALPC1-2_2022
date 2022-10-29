'''
1)	Faça um programa que receba o número de horas trabalhadas, o valor do salário 
mínimo e o número de horas extras trabalhadas. Calcule e mostre o salário a 
receber seguindo as regras abaixo:
a)	a hora trabalhada vale 1/8 do salário mínimo;
b)	a hora extra vale ¼ do salário mínimo;
c)	o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor 
da hora trabalha (apresente o valor para o usuário);
d)	a quantia a receber pelas horas extras equivale ao número de horas extras 
trabalhadas multiplicado pelo valor da hora extra(apresente o valor para o usuário);
e)	o salário a receber equivale ao salário bruto mais a quantia a receber pelas 
horas extras(apresente o valor para o usuário);
'''
print("Digite o valor do salario minimo")
salmin = float(input())
print("Digite o num de horas trabalhadas")
numhorastrab = float(input())
print("Digit eo num de horas extras")
numhorasextra = float(input())
#a)	a hora trabalhada vale 1/8 do salário mínimo;
valhora = salmin / 8
print("O valor da hora e", valhora)
#b)	a hora extra vale ¼ do salário mínimo;
valhoraextra = salmin / 4
print("O valor da hora extra e", valhoraextra)
#c)	o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor 
#da hora trabalha (apresente o valor para o usuário);
salbruto = numhorastrab * valhora
print("O valor do salario bruto e ", salbruto)
#d)	a quantia a receber pelas horas extras equivale ao número de horas extras 
#trabalhadas multiplicado pelo valor da hora extra(apresente o valor para o usuário);
valrecebhoraextra = numhorasextra * valhoraextra
print("O valor a receber de horas extras e ", valrecebhoraextra)
#e)	o salário a receber equivale ao salário bruto mais a quantia a receber pelas 
#horas extras(apresente o valor para o usuário);
salreceber = salbruto + valrecebhoraextra
print("O valor a receber e ", salreceber)