preco = float(input('Digite o preço:'))
pag = str(input('Digite o método de pagamento:')).lower()

if pag == 'cheque' or pag == 'dinheiro':
	print('O valor eh:{}'.format(preco*0.9))
elif pag == 'cartao':
	qtd = abs(int(input('Digite em quantas vezes:')))
	#print(qtd)

	if qtd == 1:
		print('O valor eh:{}'.format(preco*0.95))
	elif qtd == 2:
		print('O valor eh:{}'.format(preco))
	elif qtd >= 3:
		print('O valor eh:{}'.format(preco*1.2))
	else:
		print('Opção inválida')