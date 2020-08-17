a = int(input('Digite o valor do Primeiro Termo:'))
r = int(input('Digite o valor da Razão:'))
count = 0 
termos = 10

while count < termos:
	print('{} ->'.format(a), end=' ')
	a = a + r
	count += 1

	if count == termos:
		aux = str(input('\nDeseja aumentar a quantidade de termos?[S/N]')).upper()
		if aux == 'S':
			aux = int(input('Digite quantos termos deseja a mais:'))
			termos = termos + aux;


print('Fim')




