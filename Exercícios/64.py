
n = 0
s = 0
count = 0
while n != 999:
	n = int(input('Digite o valor do número:'))
	if n == 999:
		print('Condição de Parada satisfeita.\n')
	else: 
		s += n
		count += 1

print('Você digitou {} números e a Soma deles eh:{}'.format(count,s))
