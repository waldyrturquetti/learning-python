
altura = float(input('digite sua altura:'))
peso = float(input('digite seu peso:'))

imc = peso/altura**2
print('Seu imc eh:{:.1f}'.format(imc))

if imc<18.5:
	print('Abaixo do peso')
elif imc>=18.5 and imc<=25: # 25 >= imc >= 18.5 
	print('Peso ideal')
elif imc>25 and imc<=30:  #30 <= imc < 40
	print('Sobrepeso')
elif imc>30 and imc<=40:
	print('Obesidade')
else:
	print('Obesidade Mórbida')