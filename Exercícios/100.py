from random import randint
from time import sleep

def somaPar(valores):
	pares = []
	for c in range(5):
		if valores[c] % 2 == 0:
			 pares.append(valores[c])
	print(f'A soma dos números pares {valores} eh:',end=' ',flush = True)
	sleep(1)
	print(sum(pares))


def sorteia():
	valores = list()
	print('Sorteando os 5 valores da lista:',end=' ',flush = True)
	sleep(2)
	for c in range(5):
		valores.append(randint(0, 100)) 
	print(valores, end=' ')
	print('PRONTO!')
	somaPar(valores)


sorteia()






