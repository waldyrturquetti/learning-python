salario = float(input('Digite o salário:'))

if salario <= 1250.00:
	print('O aumento desse salário será:{:.2f} reais, resultando em um salário de {} reais'.format(salario*0.15, salario + salario*0.15))
else:
	print('O aumento desse salário será:{:.2f} reais, resultando em um salário de {} reais'.format(salario*0.1, salario + salario*0.1))