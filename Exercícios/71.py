
valor = int(input('Digite o valor a ser sacado:'))
auxValor = valor

count50 = count20 = count10 = count1 = 0

while True:
	if valor >= 50:
		valor -= 50
		count50 += 1

	elif valor >= 20:
		valor -= 20
		count20 += 1

	elif valor >= 10:
		valor -= 10
		count10 += 1

	elif valor >= 1:
		valor -= 1
		count1 += 10

	elif valor == 0:
		break

print(f'''Para {auxValor} reais, será necessário {count50} notas de 50,
{count20} notas de 20, {count10} notas de 10 e {count1} notas de 1''')
