frase = str(input('Digite uma frase:')).upper().strip()

print('ah letra A aparece:{} vezes'.format(frase.count('A')))

print('ah letra A aparece primeiro na posição:{}'.format(frase.find('A') + 1))


for i in range(len(frase) - 1 ,-1 ,-1):
	if frase[i] == 'A':
		print('ah letra A aparece por último na posição:{}'.format(i))	
		break 		

#poderiamos ter usado simplesmente um rfind() + 1 que preocura a partir da direita pra esquerda
