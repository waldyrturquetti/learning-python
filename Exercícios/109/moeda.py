def aumentar(valor=0,porc=0,parametro=False):
	valor = valor + valor*porc/100 
	if parametro is False: 
		return valor
	else:
		return moeda(valor)

def diminuir(valor=0,porc=0,parametro=False):
	valor = valor - valor*porc/100
	if parametro is False: 						#Poderia ser usado também return valor if parametro is false else moeda(valor)
		return valor
	else:
		return moeda(valor)

def dobra(valor=0,parametro=False):
	valor = valor*2
	if parametro is False: 
		return valor
	else:
		return moeda(valor)

def metade(valor=0,parametro=False):
	valor = valor/2
	if parametro is False: 
		return valor
	else:
		return moeda(valor)

def moeda(valor=0,moeda='R$'):
	 return str(f'{moeda}{valor:.2f}').replace('.',',')

