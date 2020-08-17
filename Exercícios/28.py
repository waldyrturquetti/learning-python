import random
from time import sleep

x = random.randint(0, 5)

n = int(input('digite um número entre 0 e 5:'))
print('PROCESSANDO...')
sleep(3)

if n == x:
	print('Você acertou o número')
else:
	print('Você não acertou o número, o número certo era:{}'.format(x))
