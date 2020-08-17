def fatorial(n=1, show=False):
	"""
	->Calcula o fatoria de n.
	:param n: N é o número que será calculado o fatorial.
	:param show: É opcional, seria para mostrar ou não a conta.
	:param return: Retorna o resultado do fatorial de n.
	"""
	f = 1
	for c in range(1,n+1):
		f *= c
		if show is True:
			if c < n:
				print(f' {c} ',end='x')
			else:
				print(f' {c} ',end='= ')
	
	return f



n = int(input('Digite um número:'))

op = str(input('Deseja ativar o show? [S/N]')).upper().strip()[0]
while True:
	if op == 'S' or op == 'N':
		break
	op = str(input('Deseja ativar o show? [S/N]')).upper().strip()[0]

if op == 'S':
	print(fatorial(n,True))
else:
	print(fatorial(n))
