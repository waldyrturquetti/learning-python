aluno = dict()

aluno['nome'] = str(input('nome:')).title().strip()
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}:'))

#print(aluno)

if aluno['media'] < 5.0:
	aluno['situacao'] = 'Reprovado'
elif 5.0 <= aluno['media'] < 7.0:
	aluno['situacao'] = 'Recuperação'
else:
	aluno['situacao'] = 'Aprovado'

print(f'nome igual a {aluno["nome"]}')
print(f'Média igual a {aluno["media"]}')
print(f'Situação igual a {aluno["situacao"]}\n')


'''
for k, v in aluno.items():
	print(f' - {k} é igual a {v}.')
