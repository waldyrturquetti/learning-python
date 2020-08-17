from random import randint
from time import sleep
#from operator import itemgetter

jogadores = {}

print()
print('Valores Sorteados:')
for c in range(4):
	nome = str(f'Jogador {c+1}')
	dado = randint(1, 6)
	jogadores[f'nome{c+1}'] = nome
	jogadores[f'dado{c+1}'] = dado
	sleep(1)
	print(f'O {nome} tirou {dado}')

#ranking = []
#ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # com isso ele iria colocar na ordem de maior para menor

for c1 in range(0,4):
	#print(f'c1:{c1}')
	maior = jogadores[f'dado{c1+1}']
	for c2 in range(c1,4):
		#print(f'c2:{c2}')
		atual = jogadores[f'dado{c2+1}']
		#print(f'Atual:{atual}')
		if maior < atual:
			auxDado = jogadores[f'dado{c1+1}']
			auxNome = jogadores[f'nome{c1+1}']
			jogadores[f'nome{c1+1}'] = jogadores[f'nome{c2+1}']
			jogadores[f'dado{c1+1}'] = jogadores[f'dado{c2+1}']
			jogadores[f'nome{c2+1}'] = auxNome
			jogadores[f'dado{c2+1}'] = auxDado
			maior = atual

#print(jogadores)
print()
print('++Ranking dos jogadores:++')
for c in range(4):
	nome = jogadores[f'nome{c+1}']
	dado = jogadores[f'dado{c+1}']
	sleep(1)
	print(f'{c+1}o lugar:{nome} com {dado}')

'''
for i, v in enumerate(ranking):
	print(f'  {i+1}o lugar: {v[0]} com {v[1]}.')
	sleep(1)
'''








