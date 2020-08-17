n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))

m = (n1+n2)/2

if m < 5:
 	print('aluno reprovado')
elif m>=5.00 and m<=6.90:  #poderia ser usado if 6.9 >= m >= 5:
	print('aluno de recuperação')
else:
	print('aluno aprovado')