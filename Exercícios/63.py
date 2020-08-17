ak_1 = 0
ak_2 = 1

ak_3 = ak_1 + ak_2

termos = int(input('Digite a quantidade de termos para a sequência de Fibonacci:'))


print('A sequência:')
if termos == 1:
	print('{}'.format(ak_1)) 
elif termos == 2:
	print('{} {}'.format(ak_1,ak_2))
else:
	print('{} {}'.format(ak_1,ak_2), end=' ')
	count = 3
	while count <= termos:
		print('{}'.format(ak_3), end=' ')
		ak_1 = ak_2
		ak_2 = ak_3
		ak_3 = ak_1 + ak_2

		count += 1

print('\n')
