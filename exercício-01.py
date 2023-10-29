'''Usando o arquivo texto notas_estudantes.txt escreva um programa 
que imprime o nome dos alunos que têm mais de seis notas.'''
lista_notas=[]
with open('notas_estudantes.txt','r') as arquivo:
    print('Os alunos que têm mais de seis notas são: ')
    linhas = arquivo.readlines()
    for i in range(len(linhas)):
        lista_notas=(linhas[i]).split()
        if len(lista_notas) > 6:
            print(lista_notas[0])