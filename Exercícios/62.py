a = int(input('Digite o valor do Primeiro Termo:'))
r = int(input('Digite o valor da Razão:'))
count = 0 
termos = 10

while count < termos:
	print('{} ->'.format(a), end=' ')
	a = a + r
	count += 1

	if count == termos:
		print('PAUSA')
		aux = int(input('\nQuantos termos vc deseja a mais?:'))
		if aux >= 0:
			termos = termos + aux


print('FIM')
print('Progressão realizada com {} termos mostrados:'.format(termos))




