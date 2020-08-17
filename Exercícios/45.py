import random

print('Pedra - 1, Papel - 2, Tesoura - 3')

lista = ['Pedra', 'Papel', 'Tesoura']
#print(lista) 

jogador = int(input('Qual o movimento que vc irá fazer:'))
jogador = lista[jogador - 1]
#print(jogador)
print('O jogador escolheu: {}'.format(jogador))

pc = random.randint(0, 2)
#print(pc)
pc = lista[pc]
print('O PC escolheu: {}'.format(pc))


if jogador == pc:
	print('Empate')
elif (jogador == lista[0] and pc == lista[1]) or (jogador == lista[1] and pc == lista[0]):

	if jogador == lista[0]:
		print('O PC ganhou')
	else:
		print('O jogador ganhou')

elif (jogador == lista[1] and pc == lista[2]) or (jogador == lista[2] and pc == lista[1]):

	if jogador == lista[1]:
		print('O PC ganhou')
	else:
		print('O jogador ganhou')

elif (jogador == lista[2] and pc == lista[0]) or (jogador == lista[0] and pc == lista[2]):

	if jogador == lista[2]:
		print('O PC ganhou')
	else:
		print('O jogador ganhou')


