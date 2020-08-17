cidade = input('digite o nome da cidade:')

if 'SANTO' == cidade.split()[0].upper():
	print('A cidade tem SANTO no primeiro nome')
else:
	print('A cidade tem não SANTO no primeiro nome')

'''
cidade = str(input('digite o nome da cidade:')).strip() #para tirar os espaços

print(cidade[0:5].upper() == 'SANTO')
'''


