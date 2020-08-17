from time import sleep

def contador1():
	print('='*30)
	print('Contagem de 1 até 10 em 1 em 1')
	for c in range(1,11):
		print(f'{c}',end=' ',flush=True)
		sleep(0.5)
	print('FIM!')

def contador2():
	print('='*30)
	print('Contagem de 10 até 0 em 2 em 2')
	for c in range(10,-1,-2):
		print(f'{c}',end=' ',flush=True)
		sleep(0.5)
	print('FIM!')
	print('='*30)

def contador3(inicio,fim,passo):
	auxFim = fim
	if inicio > fim: 
		if passo > 0:
			passo *= -1
		fim -= 1
	elif inicio < fim:
		if passo < 0:
			passo *= -1
		fim += 1
	
	if passo == 0:
		print('ta entrando')
		if inicio < fim:
			passo = 1
		else:
			passo = -1

	print(f'Contagem de {inicio} até {auxFim} em {abs(passo)} em {abs(passo)}')
	for c in range(inicio, fim, passo):
		print(f'{c}',end=' ',flush=True)
		sleep(0.5)
	print('FIM!')
	print('='*30)


contador1()
contador2()

inicio = int(input('Digite o inicio:'))
fim = int(input('Digite o fim:'))
passo = int(input('Digite o passo:'))

contador3(inicio, fim, passo)

