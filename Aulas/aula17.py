num = [2, 5, 9, 1]
print(num)

#Listas NÃO SÃO imutáveis
num[2] = 3
print(num)

#adicionando um valor na lista,adiciona no final
num.append(7)
print(num)

#organiza em ordem
num.sort()
print(num)

#Inverte a lista
num.sort(reverse=True)
print(num)

print(f'Essa lista tem {len(num)} elementos')

num.insert(2, 0) #Insere o valor o no index 2, e empurra os index a partir do 2 antigo para trás.
print(num)

num.pop()#remove o último elemento
print(num)

num.append(3)
print(num)
num.pop(3)#remove o objeto 3 da lista, o com index menor
print(num)

num.append(7)
#print(num)

#Sempre bom fazer a verificação para tirar elementos da lista
if 4 in num:
	#remove o objeto 7 da lista, o com index menor
	num.remove(7)
	print(num)
else:
	print('O existe o valor 4, nessa lista')

print('=-=-'*20)

#valores = [] #lista vazia
#OU
valores = list()
valores.append(5)
valores.append(4)
valores.append(9)

for c,v in enumerate(valores):
	print(f'Achei na posicação {c} da lista o valor {v}')
print('Cheguei ao final da lista')
print('=-=-'*20)

valores = []
for c in range(5):
	num = int(input('Digite um valor:'))
	valores.append(num)

for c in valores:
	print(f'{c}...',end='')
print('')
print('=-=-'*20)

#B aponta para o mesmo endereço de a, então alterar atráves de um, irá resultar na alteração dos dois.
a = [2,4,5,7]
b = a

print(f'Lista A:{a}')
print(f'Lista B:{b}')

b[2] = 10
print(f'Lista A:{a}')
print(f'Lista B:{b}')
print('=-=-'*20)

#para resolver isso 
a = [2,4,5,7]
b = a[:] #copia os valores de a, para a nova lista de b, que possui um outro endereço

print(f'Lista A:{a}')
print(f'Lista B:{b}')

b[2] = 10
print(f'Lista A:{a}')
print(f'Lista B:{b}')


