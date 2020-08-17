num = input('digite um número de 0 a 9999:')

print(range(len(num),0,-1))

for i in range(len(num)):
	if i == 0:
		print('unidade:{}'.format(num[len(num) - 1]))

	if i == 1:
		print('dezena:{}'.format(num[len(num) - 2]))

	if i == 2:
		print('centena:{}'.format(num[len(num) - 3]))

	if i == 3:
		print('milhar:{}'.format(num[len(num) - 4]))

'''
Poderia ter sido usado tbm um outro raciocinio:
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 
e dps apenas printar essas variaveis
'''
	