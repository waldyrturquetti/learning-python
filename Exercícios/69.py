#idade = []
#sexo = []
countA = 0
countB = 0
countC = 0

while True:
	auxIdade = int(input('Digite a idade da pessoa:'))
	auxSexo = str(input('Digite o sexo da pessoa:')).upper().strip()[0]
	while auxSexo != 'M' and auxSexo != 'F':
		auxSexo = str(input('Digite o sexo da pessoa:')).upper().strip()[0]

	if auxIdade > 18:
		countA += 1
	if auxSexo == 'M':
		countB += 1
	elif auxSexo == 'F' and auxIdade < 20:
		countC += 1

	op = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
	while op != 'S' and op != 'N':
		op = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
	if op != 'S':
		break

print(f'{countA} pessoas tem mais de 18 anos.')
print(f'{countB} pessoas são homens.')
print(f'{countC} pessoas são mulheres e tem menos de 20 anos.')

