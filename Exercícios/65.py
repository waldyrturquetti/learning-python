
lista = []
op = 'S'

while op =='S':
	n = int(input('Digite um número:'))
	lista.append(n)
	op = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]

print(lista)
print('Ah média entre esses números eh:{}'.format(sum(lista)/len(lista)))
print('O maior número que vc digitou eh:{}'.format(max(lista)))
print('O menor número que vc digitou eh:{}'.format(min(lista)))
