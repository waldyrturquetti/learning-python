import string

def ficha(nome='<desconhecido>', gols=0):
	string = str(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
	return string



numeros = range(10)
flag = True

print('--'*20)
nome = str(input('Nome jogador:')).title().strip()
gols = str(input('Número de gols:'))

if gols != '':			#Poderia ser usado o gols.isnumeric():
	for c in gols:
		if c not in numeros:
			flag = False
else:
	flag = False

if flag is True and nome.strip() != '':
	print(ficha(nome,gols))
elif flag is True and nome.strip() == '':
	print(ficha(gols=gols))
elif flag is False and nome.strip() != '':
	print(ficha(nome.strip()))
else:
	print(ficha())