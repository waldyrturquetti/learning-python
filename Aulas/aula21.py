
def contador(i,f,p):
	"""										#Docstring
	-> Faz uma contagem que mostra na tela
	:param i: inicio da contagem
	:param i: fim da contagem
	:param i: passo da contagem
	:return: Sem retorno 
	"""
	c = 1
	while c <= f:
		print(f'{c}',end='..')
		c += 1
	print('FIM!')

def somar(a=0, b=0, c=0):	#Parâmetros Opcionais
	s = a + b + c
	print(f'A soma vale {s}')

def teste():
	x = 4			#Variável x é local
	print(f'Na função teste n vale {n}')
	print(f'Na função teste x vale {x}')

def teste2():
	n = 6			#Essa Variável n é local
	x = 4			#Variável x é local
	print(f'Na função teste n vale {n}')
	print(f'Na função teste x vale {x}')

def teste3():
	global n		#Essa Variável n é a global agora
	n = 6
	x = 4			#Variável x é local
	print(f'Na função teste n vale {n}')
	print(f'Na função teste x vale {x}')

def somar2(a=0, b=0, c=0):	#Parâmetros Opcionais
	s = a + b + c
	return s

def fatorial(num=1):
	f = 1
	for c in range(num,0,-1):
		f *= c
	return f

def par(n=0):
	if n % 2 == 0:
		return True
	else:
		return False

#Interactive help: help()
help(print)
print('=-'*20)
help(len)
print('=-'*20)
help(input)
print('=-'*20)

#OU

print(input.__doc__)
print('=-'*20)
print(print.__doc__)
print('=-'*20)


#Docstrings
help(contador)
print('=-'*20)

#Parâmetros Opcionais
somar(3, 4, 10)
somar(8, 4)
somar()
#somar(8,5,1,7)   Desse jeito irá dar erro
somar(b=8,c=1)	#O a irá valer 0
somar(c=1,b=8)	#O a irá valer 0
print('=-'*20)

#Escopo de Variáveis
#Programa Principal
n=2						#Variável Global
print(f'No Programa Principal n vale {n}')
teste()
#print(f'No Programa Principal x vale {x}') #Irá dar erro
teste2()
print(f'No Programa Principal n vale {n}')
teste3()
print(f'No Programa Principal n agora vale {n}')
print('=-'*20)

#Retorno de Valores
resp = somar2(2,3,4)
print(f'A soma eh:{resp}')
print(f'A primeira soma vale {somar2(4,2)}, a segunda {somar2(3,1,9)} e a terceira {somar2(1)}')
print('=-'*20)

#Prática
n = int(input('Digite um número:'))
resp = fatorial(n)
print(f'O fatorial de {n} vale {resp}')
print(f'O fatorial de 1 vale {fatorial()}')

print('=-'*20)

n = int(input('Digite um número:'))
if par(n):
	print('n é par')
else:
	print('n é impar')





