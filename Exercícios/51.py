a = int(input('Digite o valor do Primeiro Termo:'))  
r = int(input('Digite o valor da razão:'))
d = a + (10 - 1) * r

for n in range(a, d + r, r): 		#range(0,9) pois ja temos um termo dos 10
	print('{}'.format(n), end=' -> ')
	#a = a + r 
	
print('Acabou')
#print('A soma dessa PG até o 10 termo eh:{}'.format(a))



