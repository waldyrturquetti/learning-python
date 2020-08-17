tempo = int(input('Quantos anos tem seu carro:'))
print('Carro Novo' if tempo <= 3 else 'Carro Velho')


nome = input('digite seu nome:')

if nome.upper() == 'WALDYR':	
	print('Que nome lindo vc tem')
else:
	print('Seu nome é tão normal')

print('Bom dia, {}'.format(nome))



n1 = int(input('digite a sua nota 1:'))
n2 = int(input('digite a sua nota 2:'))
m = (n1+n2)/2
print('Sua média eh:{}'.format(m))
if m >= 6:
	print('Sua nota é boa')
else:
	print('Sua nota precisa melhorar, estude mais')