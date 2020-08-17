for n in range(0,6):
	print('OI ')
	print(n)
print('FIM')

print('===============================================')

for n in range(6,0,-1):
	print('OI ')
	print(n)
print('FIM')

print('===============================================')

for n in range(0,7,2):
	print('OI ')
	print(n)
print('FIM')

print('===============================================')

n = int(input('Digite um número:'))
for c in range(0,n+1):
	print(c)
print('FIM')

print('===============================================')

i = int(input('inicio:'))
f = int(input('fim:'))
p = int(input('passo:'))

for c in range(i, f+1, p):
	print(c)
print('FIM')

print('===============================================')

s = 0
for c in range(0,5):
	n = int(input('Digite um número:'))
	s += n
print('FIM')
print('A soma = {}'.format(s))



