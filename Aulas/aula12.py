nome = str(input('Qual é o seu nome?'))

if nome == 'Waldyr':
	print('Que nome bonito vc tem!!!')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
	print('Seu nome é bem popular no Brasil')

elif nome == 'Willian':
	print('Que nome Gay vc tem!!') 
	
else:
	print('Que nome normal você tem')


print('Tenha um bom dia, {}'. format(nome))