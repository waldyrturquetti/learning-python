import math #importa todas as funções da biblioteca math
#from math import sqrt,floor //só importa as funções sqrt e floor da biblioteca math

num = int(input('Digite um número:'))

raiz = math.sqrt(num)

print('A raiz do numero eh:{}'.format(math.ceil(raiz))) #arredonda pra cima
print('A raiz do numero eh:{}'.format(math.floor(raiz))) #arredonda para baixo
print('A raiz do numero eh:{}'.format(raiz)) #não arredonda

import random

x = random.random() #numero aleatorio entre 0 e 1
y = random.randint(1,10) #numero aleatorio entre dois numeros inteiros, que eu defini como sendo 1 e 10

print('\n'+str(x))
print(y)