from random import randint

nPc = randint(0, 10)
#print(nPc)

nJogador = int(input('Digite um número entre [0,10]:'))
count = 1

while nPc != nJogador:
	print('Número Errad0, tente novamente:')
	nJogador = int(input('Digite um número entre [0,10]:'))
	count += 1

print('Parabens você acertou o número, com {} tentativas'.format(count))