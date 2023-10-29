'''4.) Escreva um programa para sortear os próximos times da próxima maratona de programação. 
Leia um arquivo com nome de estudantes e forme grupos de 5 pessoas.'''
import random
with open('alunos1periodo.txt','r') as files:
    listaestudante = files.readlines()
for i in range(len(listaestudante)):
    listaestudante[i] = listaestudante[i].strip()
random.shuffle(listaestudante)
grupos = []
grupoAtual = []
for nome in listaestudante:
    if len(grupoAtual) < 5:
        grupoAtual.append(nome)
    else:
        grupos.append(grupoAtual)
        grupoAtual = [nome]
if grupoAtual:
    estudantes_restantes = len(grupoAtual)
    grupos_existentes = len(grupos)
    for i in range(estudantes_restantes):
        grupo_aleatorio = i % grupos_existentes
        grupos[grupo_aleatorio].append(grupoAtual[i])
for i in range(len(grupos)):
    print(f'Grupo {i+1}: {grupos[i]}\n')