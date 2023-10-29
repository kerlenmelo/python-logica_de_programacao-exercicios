'''2. Usando o arquivo texto notas_estudantes.txt, escreva um programa que
calcula a média das notas de cada estudante e imprime o nome e a média de cada estudante.'''
with open('notas_estudantes.txt','r') as arquivo:
    alunos=[]
    listaAlunos=[]
    listaStrings = arquivo.readlines()
    for i in range(len(listaStrings)):
        alunos.append(listaStrings[i][0:-1])        #REMOVER O \n
        listaAlunos+=[(alunos[i]).split()]          #Dividir cada aluno e suas notas em listas
for x in range(len(listaAlunos)):
    print(f'Aluno: {listaAlunos[x][0]}')   #Pegando cada nome, em cada lista, os nomes sempre serão o indice [0]
    notas = (listaAlunos[x][1:])
    soma = 0
    for valor in notas:
        soma += int(valor)
    print(f'Média: {soma / (len(notas)):.2f}\n')