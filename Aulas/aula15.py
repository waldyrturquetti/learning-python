
n = s = 0

while True:
	n = int(input('Digite um número:'))
	if n == 999:
		break
	s += n

print('A soma vale:{}'.format(s))
	
#Disponível a partir do python 3.6
print(f'A soma vale:{s}') #python 3.6+


nome = 'José'
idade = 33
salario = 975.3
print(f'O {nome:20} tem {idade} anos e ganha {salario:.2f} reais.')#python 3.6+
print('O {:20} tem {} anos e ganha {:.2f} reais.'.format(nome, idade,salario))#python 3
print('O %s tem %d anos e ganha %.2f reais.' %(nome, idade, salario))#python 2 
