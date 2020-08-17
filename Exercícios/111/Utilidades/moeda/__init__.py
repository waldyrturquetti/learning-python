def aumentar(valor=0,porc=0,parametro=False):
	valor = valor + valor*porc/100 
	if parametro is False: 
		return valor
	else:
		return moeda(valor)

def diminuir(valor=0,porc=0,parametro=False):
	valor = valor - valor*porc/100
	if parametro is False: 
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

def resumo(valor=0,aum=0,dim=0):
	print('='*20)
	print('  RESUMO DO VALOR  ')
	print('='*20)
	print(f'{"Preço analisado:":<10}{moeda(valor):>10}')
	print(f'{"Dobro do preço:":<10}{dobra(valor,True):>11}')
	print(f'{"Metade do preço:":<10}{metade(valor,True):>10}')
	print(f'{aum}{"% de aumento:":<10}{aumentar(valor,aum,True):>11}')
	print(f'{dim}{"% de reducao:":<10}{diminuir(valor,dim,True):>11}')


