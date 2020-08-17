from random import randint

print('='*20)
print('JOGO DO PAR OU ÍMPAR')
print('='*20)

count = 0
while True:
	nJogador = int(input('Digite um número:'))
	nPc = randint(0, 11)
	op = str(input('Você escolhe Par ou Ímpar [P/I]:')).upper().strip()[0]
	while op not in 'PI':
		op = str(input('Você escolhe Par ou Ímpar [P/I]:')).upper().strip()[0]

	print(f'Você jogou {nJogador} e o Computador jogou {nPc}. Total é {nJogador+nPc}, deu', end=' ')
	print('Par' if (nJogador + nPc) % 2 ==	0 else 'Ímpar')

	if (nJogador + nPc) % 2 ==	0:
		if op == 'P':
			print('Parabéns, Você acerteu!!!')
			count += 1
		else:
			print('Você perdeu')
			break
	else:
		if op == 'I':
			print('Parabéns, Você acerteu!!!')
			count += 1
		else:
			print('Você perdeu')
			break

print(f'GAME OVER, Você acertou {count} vezes')


