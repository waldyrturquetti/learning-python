pessoas = []
dados = []

while True:
	dados.append(input('Digite o nome:'))
	dados.append(float(input('Digite o peso:')))
	pessoas.append(dados[:])
	dados.clear()

	while True:
		op = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
		if op == 'N' or op == 'S':
			break

	if op == 'N' and op != 'S':
		break

print()
print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'As pessoas mais pesadas são:',end=' ')
maior = pessoas[0][1]
for p in pessoas:
	if maior < p[1]:
		maior = p[1]
for p in pessoas:
	if maior == p[1]:
		print(f'{p[0]} ',end=' ')
print(f'pessando {maior}')

print(f'As pessoas menos pesadas são:',end=' ')
menor = pessoas[0][1]
for p in pessoas:
	if menor > p[1]:
		menor = p[1]
for p in pessoas:
	if menor == p[1]:
		print(f'{p[0]} ',end=' ')
print(f'pessando {menor}')


