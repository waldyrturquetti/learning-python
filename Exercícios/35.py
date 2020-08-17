
l1 = float(input('Digite o valor do lado 1:'))
l2 = float(input('Digite o valor do lado 2:'))
l3 = float(input('Digite o valor do lado 3:'))

lista = [l1, l2, l3]
print(lista)

lmin1 = min(lista)
#print(lmin1)

del(lista[lista.index(lmin1)])
#print(lista)

lmin2 = min(lista)
#print(lmin2)

if (lmin1 + lmin2) > max(lista):
	print('Essas retas podem formar um triângulo')
else:
	print('Essas retas não podem formar um triângulo')


