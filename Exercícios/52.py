num = int(input('Digite um número:'))
aux = True

if num == 1 or num == 2:
	print('O número {} é Primo.'.format(num))

for c in range(num-1, 1, -1):
	if num % c == 0:
		aux = False
		break

if aux is True:
	print('O número {} é Primo.'.format(num))
else:
	print('O número {} não é Primo.'.format(num))
