
#__init__ é um módulo que pertence ao pacote numeros e numeros pertence ao pacote aula22_Pacotes

def fatorial(n=1):
	f=1
	for c in range(1,n+1):
		f *= c
	return f

def dobro(n):
	return n*2

def triplo(n):
	return n*3