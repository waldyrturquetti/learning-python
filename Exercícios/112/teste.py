from Utilidades import moeda
from Utilidades import dado

valor = str(input('Digite o preço: R$')).split()
if dado.verifica(valor):
	moeda.resumo(dado.passaFlaot(valor),60,40)
else:
	print(f'\033[31mERRO!!"{valor}" é um preço inválido\033[m')


'''
Poderia ter sido feito dessa outa maneira mais simples
valor = leiaDinheiro('Digite o preço: R$')
moeda.resumo(dado.passaFlaot(valor),60,40)
'''

