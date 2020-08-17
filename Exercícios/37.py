
op = input('digite a opção desejada:')

num = int(input('Qual o valor que desejada converter:'))

if op == '1':
	print('O valor {} eh igual a {} em binário'.format(num,bin(num)[2:]))
elif op == '2':
	print('O valor {} eh igual a {} em Octal'.format(num,oct(num)[2:]))
elif op == '3':
	print('O valor {} eh igual a {} em Hexadecimal'.format(num,hex(num)[2:]))
else:
	print('Opção inválida.')