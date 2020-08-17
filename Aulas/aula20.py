#Função
def mostraLinha():
	print('--'*20)

def mensagem(msg):
	print('--'*20)
	print(msg)
	print('--'*20)

def soma(a, b):
	print(f'A = {a} e B = {b}')
	s = a + b
	print(f'A soma de A + B = {s}')

#conceito de empacotamento
def contador(*num):			#Dessa maneira desempacotamos, sendo num uma tupla com os valores na chamada da função	
	print(num)				
	tam = len(num)
	print(f'O tamnha da tupla eh:{tam}')
	print(f'A soma da tupla eh:{sum(num)}')

def dobra(lista):
	pos = 0
	while pos<len(lista):
		lista[pos] *= 2
		pos += 1


#Programa Principal
print('--'*20)
print('CURSO EM VÍDEO')
print('--'*20)

mostraLinha()
print('APRENDA PYTHON')
mostraLinha()

mensagem('WALDYR TURQUETTI')

print('==='*20)

a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)

mostraLinha()

soma(4,5)
soma(8,9)	#Nesse caso por default o primeiro é a e o segundo é b
soma(2,1)
soma(b=4, a=3)


print('==='*20)

contador(8,1,2,3)
contador(2,3,6)

print('==='*20)

valores = [7,3,2,9,4]
print(valores)			#É uma passagem por referência. Diferente de contador que empacota os valores transformando em uma tupla
dobra(valores)
print(valores)


