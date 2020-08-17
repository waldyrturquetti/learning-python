pessoa = {}
lista = list()

while True:
	pessoa['nome'] = str(input('Nome:')).title().strip()
	pessoa['sexo'] = str(input('Sexo:')).strip().upper()[0]
	
	while True:
		if pessoa['sexo'] == 'M'or pessoa['sexo'] == 'F':
			break
		print('ERRO!! Digite apenas M ou F')
		pessoa['sexo'] = str(input('Sexo:')).strip().upper()[0]

	pessoa['idade'] = int(input('idade:'))
	lista.append(pessoa.copy())

	while True:
		op = str(input('Deseja Continuar [S/N]?')).strip().upper()[0]
		if op == 'N'or op == 'S':
			break
		print('ERRO!! Digite apenas S ou N')
	if op == 'N':
		break
print('=-='*20)
print(lista)
print('=-='*20)

print(f'Foram cadastradas {len(lista)} pessoas')

#print('=-='*20)
media = 0
for c in range(len(lista)):
	media = lista[c]['idade'] + media
media = media/len(lista)
print(f'A média de idade eh:{media:.2f} anos')

print('As mulheres cadastradas foram:',end=' ')		#Iria funcionar assim também
for c in range(len(lista)):							#for p in lista:
	if lista[c]['sexo'] == 'F':						#	if p['sexo'] = 'F':
		print(f'{lista[c]["nome"]}', end=' ')

print()
print('As pessoas que estão com idade acima da média:')
for c in range(len(lista)):
	if lista[c]['idade'] > media:
		print(lista[c])
print('Programa Encerrado')






