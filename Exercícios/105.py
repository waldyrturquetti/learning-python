def notas(numeros, sit=False):
	"""
	->Função para anailisar notas de vários alunos
	:param numeros: lista com as notas dos aluno, não pode ser estar vazia.
	:param sit:Se True irá informar a situação do aluno (Valor opcional).
	:param return: retorna o dicionário com a informação das notas do aluno.
	"""

	dicionario = dict()
	dicionario['Quantidade'] = len(numeros)
	dicionario['Maior'] = max(numeros)
	dicionario['Menor'] = min(numeros)
	dicionario['Média'] = sum(numeros)/len(numeros)
	if sit is True:
		if dicionario['Média'] <= 5:
			dicionario['situação'] = 'RUIM'
		elif 5 < dicionario['Média'] < 7:
			dicionario['situação'] = 'REGULAR'
		else:
			dicionario['situação'] = 'BOM'

	return dicionario

numeros = []

while True:
	num = float(input('Digite um número:'))
	numeros.append(num)

	while True:
		op = str(input('Deseja adicionar mais um número? [S/N]')).strip().upper()[0]
		if op == 'N' or op == 'S':
			break

	if op == 'N':
		break


#print(numeros)

while True:
	op = str(input('Deseja ver a situação? [S/N]')).strip().upper()[0]
	if op == 'N' or op == 'S':
		break


if op == 'S':
	print(notas(numeros,True))
else:
	print(notas(numeros))


