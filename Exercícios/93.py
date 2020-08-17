jogador = dict()
gols = list()

jogador['nome'] = str(input('Digite o nome do jogador:')).title().strip()
qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

for c in range(qtd):
	gol = int(input(f'Quantos gols na partida {c+1}?'))
	gols.append(gol)

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-='*20)
print(jogador)

print('-='*20)
print(f'O Campo nome tem o valor {jogador["nome"]}')
print(f'O Campo gols tem o valor {jogador["gols"]}')
print(f'O Campo total tem o valor {jogador["total"]}')

'''
for k, v in jogador.items():
	print(f'  - O campo {k} tem o valor {v}')
'''

print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {qtd} partidas.')
for c in range(qtd):
	print(f'   => Na partida {c+1}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols')

'''
for i, v in enumerate(jogador['gols']):
	print(f'  => Na partida {i} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
'''