'''1. Crie um arquivo notas_estudantes.txt com as seguintes notas dos alunos de uma turma:
jose 10 15 20 30 40
pedro 23 16 19 22
suzana 8 22 17 14 32 17 24 21 2 9 11 17
gisela 12 28 21 45 26 10
joao 14 32 25 16 89
'''
with open ('notas_estudantes.txt','w') as notas:
    notas.write('jose 10 15 20 30 40\n')
    notas.write('pedro 23 16 19 22\n')
    notas.write('suzana 8 22 17 14 32 17 23 21 2 9 11 17\n')
    notas.write('gisela 12 28 21 45 26 10\n')
    notas.write('joao 14 32 25 16 89')
    notas.seek(0)
    