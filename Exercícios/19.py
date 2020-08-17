import random

aluno1 = input('digite o nome do aluno 1:')
aluno2 = input('digite o nome do aluno 2:')
aluno3 = input('digite o nome do aluno 3:')
aluno4 = input('digite o nome do aluno 4:')

lista = []

lista.append(aluno1)
lista.append(aluno2)
lista.append(aluno3)
lista.append(aluno4)

print(lista)

print('O aluno sorteado foi:{}'.format(lista[ random.randint(0,4) ])) #poderia ter sido usado o random.choice(lista)


