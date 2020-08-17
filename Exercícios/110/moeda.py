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
	print('='*30)
	print('RESUMO DO VALOR'.center(30))
	print('='*30)
	print(f'{"Preço analisado:":<10} \t{moeda(valor)}')
	print(f'{"Dobro do preço:":<10} \t{dobra(valor,True)}')
	print(f'{"Metade do preço:":<10} \t{metade(valor,True)}')
	print(f'{aum}{"% de aumento:":<10} \t{aumentar(valor,aum,True)}')
	print(f'{dim}{"% de reducao:":<10} \t{diminuir(valor,dim,True)}')


