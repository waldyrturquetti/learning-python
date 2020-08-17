valorCasa = float(input('Digite o valor da Casa:'))
salario = float(input('Digite o valor do seu salário:'))
anos = int(input('Digite quantos anos vc pretende pagar:'))

prestacao = valorCasa/(anos * 12)
print(prestacao)

if salario*0.3 >= prestacao:
	print('Empréstimo aceito')
else:
	print('Empréstimo negado')

