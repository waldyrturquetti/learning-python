
times = ('Athetico Paranaense', 'Atlético - GO', 'Atlético - MG', 'Bahia', 'Botáfogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Vasco da Gama')
print('=-='*20)
print(times)

print('=-='*20)
print(f'Os primeiros 5 colocados são:{times[:5]}')
print('=-='*20)
print(f'Os 4 últimos colocados são:{times[-4:]}')
print('=-='*20)
print(f'Os times em ordem alfabética são:{sorted(times)}')
print('=-='*20)

if 'Chapecoense' in times:
	Print(f'O Chapecoense está na {times.index(Chapecoense)}')
else:
	print('O Chapecoense não esta na lista, então vamos falar da posição do Corinthians.')
	aux=times.index('Corinthians') + 1
	print(f'O Corinthians está na {aux} posição') #No lugar do aux poderia colocar o times.index("Corinthians") + 1, com aspas duplas


