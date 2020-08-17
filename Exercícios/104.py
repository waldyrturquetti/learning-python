
def leiaInt(strig):
	while True:
		flag = True
		numeros1 = range(10)
		numeros2 =  [str(val) for val in numeros1]
		#print(numeros1)
		#print(numeros2)

		n = str(input(strig))		#Poderia ser usado tbm o if n.isnumeric():
		for c in n:					
			if c not in numeros2:  #Poderia ser usado o for int(c) not in numeros1:
				flag = False
				#print('False')
			#else:
			#	flag = True
			#	print('True')
		if flag is True:
			#retorno = int(n)
			#return retorno
			return int(n)
		else:
			print('\033[0;31mErro!! Digite um número válido inteiro.\033[m')


n = leiaInt('Digite um número:')
print(f'O número que você digitou foi o {n}')