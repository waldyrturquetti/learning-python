nome = input('Digite seu nome completo:') #se usassemos o str(input()).strip já corta todos os espaços do inicio e final

nome1 = str(input('Digite seu nome completo:')).strip()
print(nome1)

print('O nome inteiro em maisculo:{}'.format(nome.upper()))
print('O nome inteiro em minusculo:{}'.format(nome.lower()))

nome2 = ''.join(nome.split())
#print(nome2)
print('A quantidade de letras sem os espaços:{}'.format(len(nome2))) #poderiamos ter contato quantass letras tinha no total 
																	#e fazer menos uma conta de quantos espaços


nome3 = nome.split()[0]
print('A quantidade de letras do primeiro nome:{}'.format(len(nome3)))