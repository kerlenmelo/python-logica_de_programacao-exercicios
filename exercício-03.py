'''3.) Usando o arquivo texto notas_estudantes.txt, escreva um programa que
calcula a nota mínima e máxima de cada estudante e imprima o nome de cada aluno 
junto com a sua nota máxima e mínima.'''
with open('notas_estudantes.txt','r') as arquivo:
    alunos = []
    listaAlunos = []
    listaString = arquivo.readlines()
    for i in range(len(listaString)):
        alunos.append(listaString[i][0:-1])
        listaAlunos += [(alunos[i]).split()]
print(listaAlunos)
for qtd in range(len(listaAlunos)):
    notas = []
    for num in (listaAlunos[qtd][1:]):
        notas.append(int(num))
    maiorNota = notas[0]
    menorNota = notas[0]
    for num in notas:
        if num > maiorNota:
            maiorNota = num
        if num < menorNota:
            menorNota = num
    print(f'Aluno: {listaAlunos[qtd][0]}\nA maior Nota: {maiorNota}\nA menor nota: {menorNota}\n')