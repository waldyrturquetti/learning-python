
sexo = ''
count = 0

while sexo != 'M' and sexo !='F':
	if count > 0:
		print('Entrada Inválida, digite novamente')
	sexo = str(input('Digite o sexo da pessoa [M/F]:')).upper().strip()
	count += 1

print('FIM')
