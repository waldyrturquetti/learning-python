def ajudaPython(nome):
	print('\033[30;44m')
	print('--'*20)
	print(f'Acessando o manual do comando \'{nome}\'')
	print('--'*20)
	print('\033[m')

	print('\033[7;30m')
	help(nome)
	print('\033[m')

while True:
	print('\033[30;42m')
	print('--'*20,)
	print('SISTEMA DE AJUDA PYTHON')
	print('--'*20)
	print('\033[m')

	nome = str(input('Função ou Biblioteca >'))
	print()
	if nome.upper() == 'FIM':
		break
	ajudaPython(nome)

print('\033[0;30;41m')
print('--'*20)
print('Até Logo!')
print('--'*20)
print('\033[m')