
totalGasto = count1 = 0
menor = -1

while True:
	nome = str(input('Digite o nome do Produto:')).title().strip()
	preco = float(input('Digite o valor do Produto:'))

	if menor == -1 or menor > preco:
		menor = preco
		nomeMenor = nome

	totalGasto += preco

	if preco > 1000:
		count1 += 1

	op = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
	while op != 'S' and op != 'N':
		op = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
	if op == 'N':
		break

print(f'O total gasto na compra foi {totalGasto} reais')
print(f'{count1} produtos custam mais que 1000 reais')
print(f'O Produto mais barato foi {nomeMenor} custando {menor} reais')

print('\n{:-^40}'.format('FIM DO PROGRAMA '))

