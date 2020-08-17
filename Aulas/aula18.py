teste = list()
teste.append('Waldyr')
teste.append(20)
print(teste)

galera = []
galera.append(teste)
print(galera)

teste[0] = 'Maria'
teste[1] = 25
galera.append(teste)
#Virá no caso uma lista com duas posições e cada posição será uma lista com maria e 25, pois apontamos pro msm nó nas duas posições da lista 
print(galera)

print('=-='*20)
teste[0] = 'Waldyr'
teste[1] = 20
galera = []
galera.append(teste[:]) # com isso fazemos uma copia do conteudo do nó apontado por teste
teste[0] = 'Maria'
teste[1] = 25
galera.append(teste[:])
print(galera)

print('=-='*20)
galera = [['João',19], ['Ana', 33], ['Joaquin',13], ['Maria', 25]]
print(galera)
print(galera[0])
print(galera[0][0]) #Primeiro-[]:Representa qual o conteúdo(index) da lista de fora(galera). Segundo-[]:Representa qual será o conteúdo da lista de dentro
print(galera[0][1])
print(galera[2][1])

for p in galera:
	print(f'{p[0]} tem {p[1]} anos')

print('=-='*20)
galera = []
dados = list()
for c in range(3):
	dados.append(input('Nome:'))
	dados.append(int(input('Idade:')))
	galera.append(dados) #Irá geras três listas vazias, pois damos clear no msm nó as três vezes
	dados.clear()

print(galera)

print('=-='*20)
galera = []
dados = list()
for c in range(3):
	dados.append(input('Nome:'))
	dados.append(int(input('Idade:')))
	galera.append(dados[:])
	dados.clear()

print(galera)

maior = 0
menor = 0
for p in galera:
	if p[1] >= 21:
		print(f'{p[0]} eh maior de Idade')
		maior += 1
	else:
		print(f'{p[0]} eh menor de Idade')
		menor += 1
print(f'Temos {maior} maiores de idade e {menor} menores de idade')