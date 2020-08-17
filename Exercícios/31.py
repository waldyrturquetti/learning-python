dist = float(input('Digite a distância da viagem:'))

if dist <= 200.00:
	print('O custo da viagem eh:{:.2f}'.format(dist*0.50))
else:
	print('O custo da viagem eh:{:.2f}'.format(dist*0.45))

''' Poderfia ser feito dessa maneira tbm
preco = dist * 0.5 if dist <= 200 else dist*0.45
print('O custo da viagem eh:{:.2f}'.format(preco))
