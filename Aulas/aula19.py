'''
Tuplas ()
Listas []
Dicionários {}
'''
pessoas = {'nome':'Waldyr', 'sexo':'M', 'idade':20}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print()
for k in pessoas.keys():
	print(k)
print()
for k in pessoas.values():
	print(k)
print()
for k, v in pessoas.items():
	print(f'{k} = {v}')

pessoas['nome'] = 'Leandro'
print()
for k, v in pessoas.items():
	print(f'{k} = {v}')

del pessoas['sexo']
print()
for k, v in pessoas.items():
	print(f'{k} = {v}')

pessoas['sexo'] = 'M'
pessoas['peso'] = 110.5

print()
for k, v in pessoas.items():
	print(f'{k} = {v}')

print('=-=-'*20)

brasil = []
estado1 = {'uf':'São Paulo', 'sigla':'SP'}
estado2 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}

brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['sigla'])

print('=-=-'*20)

estado = dict()
brasil = list()

for c in range(0,3):
	estado['uf'] = str(input('Unidade Federativa:'))
	estado['sigla'] = str(input('Sigla do Estado:'))
	brasil.append(estado.copy()) 	#O estado[:] não funciona com dicionários, ou seja, dicionário não aceita fatiamente

for e in brasil:
	for v in e.values():
		print(v, end=' ')
	print()

