from datetime import datetime

pessoa = dict()

nome = str(input('Nome:')).title().strip()
pessoa['nome'] = nome
anoNasc = int(input('Ano de Nascimento:'))
idade = datetime.now().year - anoNasc
pessoa['idade'] = idade
ctps = abs(int(input('Número da CTPS (digite 0 se não possuir):')))
pessoa['ctps'] = ctps

if ctps != 0:
	pessoa['anoContr'] = int(input('Ano de Contratação:'))
	pessoa['salario'] = int(input('Salário:'))
	pessoa['anoAposen'] = pessoa['anoContr'] + 35 - anoNasc
	print('=-'*20)
	print(f'Nome tem o valor de {pessoa["nome"]}')
	print(f'idade tem o valor de {pessoa["idade"]}')
	print(f'CTPS tem o valor de {pessoa["ctps"]}')
	print(f'Contratação tem o valor de {pessoa["anoContr"]}')
	print(f'Salário tem o valor de {pessoa["salario"]}')
	print(f'Aposentadoria tem o valor de {pessoa["anoAposen"]}')
else:
	print('=-'*20)
	print(f'- Nome tem o valor de {pessoa["nome"]}')
	print(f'- idade tem o valor de {pessoa["idade"]}')
	print(f'- CTPS tem o valor de {pessoa["ctps"]}')

'''
for k, v in pessoa.items():
	print(f'  -{k} tem o valor {v}')
'''
	


