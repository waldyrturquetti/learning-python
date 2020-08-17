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

if idade<=9:
	print('Mirin')
elif idade<=14:
	print('Infantil')
elif idade<=19:
	print('Junior')
elif idade<=20:
	print('Sênior')
else:
	print('Master')