jogador = dict()
gols = list()
jogadores = []

while True:
	jogador['nome'] = str(input('Digite o nome do jogador:')).title().strip()
	qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

	for c in range(qtd):
		gol = int(input(f'Quantos gols na partida {c+1}?'))
		gols.append(gol)

	jogador['gols'] = gols[:]
	jogador['total'] = sum(gols)
	gols.clear()
	jogadores.append(jogador.copy())

	while True:
		op = str(input('Deseja Continuar [S/N]?')).strip().upper()[0]
		if op == 'N'or op == 'S':
			break
	if op == 'N':
		break
print('-='*20)

print(f'{"Cod":<4}{"Nome":<4}{"Gols":>15}{"Total":>15}')					#for i in jogador.keys():
																				#print(f'{i<15}',end='')
for pos,c in enumerate(jogadores):											
	print(f'{pos:<4}{c["nome"]:<10}{" ":^5}{c["gols"]}{c["total"]:>6}')			#print(f'{k:>4} ',end='')
																				#for d in c.values():
print('-='*20)																		#print(f'{str(d):<15}',end=' ')


op = int(input('Mostrar os dados de qual jogador (999 para sair):'))
while op != 999:
	if op in range(len(jogadores)):
		print(f'--Levantamento do jogador {jogadores[op]["nome"]}:')
		for c in range(len(jogadores[op]['gols'])):										#for i, g enumerate(jogadores[op]['gols']):
			print(f'   => Na partida {c+1}, fez {jogadores[op]["gols"][c]} gols.')			#print(f'	No jogo {i+1} fez {g} gols')
		print(f'Foi um total de {jogadores[op]["total"]} gols')
		print('-='*20)		
	else:
		print('Erro!! jogador não existe no sistema')

	op = int(input('Mostrar os dados de qual jogador:'))

