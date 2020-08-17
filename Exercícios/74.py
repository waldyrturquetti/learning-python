from random import randint

n1 = randint(0, 101) 
n2 = randint(0, 101)
n3 = randint(0, 101)
n4 = randint(0, 101)
n5 = randint(0, 101)

tupla = (n1, n2, n3, n4, n5)

print(tupla)

print(f'O maior valor da tupla eh:{max(tupla)}')
print(f'O menor valor da tupla eh:{min(tupla)}')

#Uma outra maneira de formar a tupla
'''
tupla = (randint(0, 101), randint(0, 101), randint(0, 101), randint(0, 101), randint(0, 101))
'''