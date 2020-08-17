import datetime

anoAtual = datetime.date.today().strftime("%Y")
#print(anoAtual)
anoAtual = int(anoAtual)

count1 = 0
count2 = 0

for c in range(0,7):
	
	AnoNasc = int(input('Digite o ano de nascimento da pessoa {}:'.format(c)))
	if (anoAtual - AnoNasc) >= 21:
		count1 += 1
	else:
		count2 += 1


print('{} pessoas já atingiram ou vão atingir esse ano a maioridade'.format(count1))
print('{} pessoas ainda não atingiram a maioridade'.format(count2))





