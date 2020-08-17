
def escreva(texto):
	aux = len(texto)
	print('-'*(aux+2))
	print(f' {texto} ')
	print('-'*(aux+2))

texto = str(input('Digite um texto qualquer:')).strip()
escreva(texto)