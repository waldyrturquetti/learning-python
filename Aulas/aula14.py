c = 1

while c < 10:
	print(c)
	c = c + 1

print('Fim')

print('=========================================================')

n = 1
while n != 0:
	n = int(input('Digite um número:'))
print('Fim')

print('=========================================================')

n = 1
r = 's'
while r == 's':
	n = int(input('Digite um número:'))
	r = str(input('Deseja Continuar [s/n]:')).lower()
print('Fim')

print('=========================================================')

n = 1
par = impar = 0
while n != 0:
	n = int(input('Digite um número:'))
	if n % 2 == 0:
		par += 1
	else:
		impar += 1
print('Você digitou {} numeros pares e numeros impares {}'.format(par, impar))



