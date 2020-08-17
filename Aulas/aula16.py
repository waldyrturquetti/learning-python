#Tuplas São imutáveis

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # == lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

print(lanche)
print(lanche[1])
print(lanche[0])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(len(lanche))
print(sorted(lanche)) #organiza em ordem
print(lanche)

#Irá dar erro, pois as tuplas são imutáveis
#lanche[1] = 'Refrigerante'

print('-'*20)
for comida in lanche:
	print(f'Eu vou comer {comida}')
print('Comi pra caramba')

print('-'*20)
for count in range(0,len(lanche)):
	print(f'Eu vou comer {lanche[count]}, na posição {count}')
print('Comi pra caramba')

print('-'*20)
for pos, comida in enumerate(lanche):
	print(f'Eu vou comer {comida}, na posição {pos}')
print('Comi pra caramba')

print('-'*20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b 
print(c)
d = b + a
print(d)
print(c.count(5))
print(c.count(4))
print(c.index(8))
print(c.index(2))
print(c.index(5, 1)) #começa da posição 1


pessoa = ('Waldyr', 20, 'M', 110.5)
print(pessoa)
del(pessoa)
#print(pessoa) irá dar erro , pois excluimos a tupla , e só podemos apagar a tupla inteira e não partes da tupla


