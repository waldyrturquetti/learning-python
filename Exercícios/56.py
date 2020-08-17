
nome = []
idade = []
sexo = []
for c in range(0,4):
	#nomeAux = input('Digite o nome da pessoa {}:'.format(c+1))
	nome.append(str(input('Digite o nome da pessoa {}:'.format(c+1))).strip())
	idade.append(int(input('Digite a idade da pessoa {}:'.format(c+1))))
	sexo.append(str(input('Digite o sexo da pessoa {} [M/F]:'.format(c+1))).upper().strip())

#for c in range(0,4):
#	print('Pessoa {} - Nome:{}, idade:{}, Sexo:{}'.format(c+1, nome[c], idade[c], sexo[c]))

print('A media da Idade das pessoas eh:{:.2f}'.format(sum(idade)/4))

maiorIdadeM = 0;
for c in range(0,4):
	if sexo[c] in 'M':
		if maiorIdadeM < idade[c]:
			maiorIdadeM = idade[c]

print('O homem idade do homem mais velho eh:{}'.format(maiorIdadeM))

countMulheres = 0 
for c in range(0,4):
	if sexo[c] in 'F':
		if idade[c] < 20:
			countMulheres += 1

print('A quantidade de mulheres com menos de 20 anos eh:{}'.format(countMulheres))



