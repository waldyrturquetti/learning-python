numeros = ('zero' ,'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'cartoze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

#print(range(0,21))

while True:
	num = int(input('Digite um número entre 0 e 20:'))
	if num not in range(0,21):
		print('Valor incorreto, digite novamente.')
	else:
		break

print(f'Você digitou o número {numeros[num]}')





