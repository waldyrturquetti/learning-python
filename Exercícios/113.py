def leiaInt(string):
	while True:
		try:
			n = int(input(string))		
		except KeyboardInterrupt:
			print('\n\033[0;31mO usuário preferiu não informar os dados do número inteiro\033[m')
			return 0
		except: 
			print(f'\033[0;31mErro!! Por favor, digite um número válido inteiro\033[m')
		else:
			return n


def leiaFloat(string):
	while True:
		try:
			n = float(input(string))		
		except KeyboardInterrupt:
			print('\n\033[0;31mO usuário preferiu não informar os dados do número decimal\033[m')
			return 0
		except: 
			print(f'\033[0;31mErro!! Por favor, digite um número válido inteiro\033[m')
			continue
		else:
			break

	return n




n1 = leiaInt('Digite um número inteiro:')
n2 = leiaFloat('Digite um número decimal:')
print(f'O número inteiro que você digitou foi o {n1} e o real foi {n2:.2f}')
