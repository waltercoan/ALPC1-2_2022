'''
Implemente um programa para controlar o 
numero de crianças em uma creche. Para 
isso solicite o número de turmas, e 
para CADA TURMA solicite o número da 
sala, o numero de alunos matriculados 
e sexo de cada uma das crianças 
(M – Masculino, F – Feminino). 
Calcule e apresente em tela:
a. Número total de crianças na creche.
b. Média de alunos considerando todas as salas.
c. O numero da sala com o maior número de meninos.
d. O numero da sala com o menor número de meninas.
'''
print("Digite o numero de turmas")
numturmas = int(input())

contatotal = 0
omaiornummeninos = 0
salamaiornumero = 0
for turma in range(numturmas):
    print("Turma: ", turma+1)
    print("Digite o num da sala")
    sala = int(input())
    print("Digite o numero de alunos")
    numalunos = int(input())
    contameninos = 0
    for aluno in range(numalunos):
        print("Aluno: ", aluno+1)
        print("Digite o sexo m/f")
        sexo = input()
        if sexo == 'm' or sexo == "M":
            contameninos += 1
        #Número total de crianças na creche.
        contatotal += 1
        #c. O numero da sala com o maior número de meninos.
    if contameninos > omaiornummeninos:
        omaiornummeninos = contameninos
        salamaiornumero = sala
print("O numero total de crianças e: ", contatotal)
#b. Média de alunos considerando todas as salas.
media = contatotal / numturmas
print("Num medio de alunos por turma e :", media)
print("A sala ", salamaiornumero, " possui maior numero de meninos")
