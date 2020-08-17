from time import sleep
from random import randint

jogos = []
dados = []

print('-'*20)
print(f'{"JOGO DA MEGA":^20}')
print('-'*20)

qtd = int(input('Digite a quantos jogos deseja fazer:'))
qtd = abs(qtd)

print('=-='*3,'SORTEANDO OS {qtd} JOGOS','=-='*3)

for c in range(qtd):
	for c2 in range(6):
		while True:
			num =  randint(1, 61)
			if num not in dados: 
				break

		dados.append(num)
	jogos.append(dados[:])
	dados.clear()

#print(jogos)

for c in range(qtd):
	print(f'JOGO {c+1} : {jogos[c]}')
	sleep(1)

print('BOA SORTE')

