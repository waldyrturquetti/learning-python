frase = str(input('Digite uma frase:')).lower()
#print(frase)

lista = frase.split()
#print(lista)

frase = ''.join(lista)
print(frase)

frase2 = frase

i=0
n=len(frase2)
flag = True

for c in range(n-1, -1, -1):
	if frase[i] != frase2[c]:
		flag = False
	i += 1

if flag is True:
	print('Ah frase é um políndromo')
else:
	print('Ah frase não é um políndromo')

