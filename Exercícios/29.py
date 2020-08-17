vel = float(input('Digite o valor da velocidade do carro:'))

if vel > 80.00:
	print('Vocẽ foi multado...')
	print('O valor da multa eh:{} reais.'.format((vel - 80.00) * 7.00))