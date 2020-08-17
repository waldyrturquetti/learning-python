from datetime import datetime

aux = input('Informe o dia do nascimento:')
dataNasc = aux + '/'
aux = input('Informe o mês do nascimento:')
dataNasc = dataNasc + aux + '/'
aux = input('Informe o ano do nascimento:')
dataNasc = dataNasc + aux
#print(dataNasc)

dataNasc = datetime.strptime(dataNasc, '%d/%m/%Y').date()
#print(dataNasc)

dataAtual = datetime.now().date()
#print(dataAtual)

idade = abs((dataAtual - dataNasc).days)
#print(idade)
idade = idade // 365


if idade == 18:
	print('Está na hora de se alistar')
elif idade > 18:
	print('Já passou o tempo de se alistar')
	print('Já se passaram {} anos do tempo de alistamento'.format(idade - 18))
else:
	print('Ainda não está na hora de se alistar')
	print('Ainda faltam {} anos do tempo de alistamento'.format(18 - idade))