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

x = random.randint(3,4)
print(x)

lista2 = []

for n in range(4):
	#print(n)
	x = random.randint(n,3)
	lista2.append(x)
	#print(lista2)
	aux = lista[n]
	lista[n] = lista[x]
	lista[x] = aux

#Simplesmente poderiams ter usado a random.shuffle(lista)
#random.shuffle(lista)

print('Os alunos nas ordens sorteadas são:{}'.format(lista)) 
