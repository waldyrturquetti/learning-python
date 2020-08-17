

def voto(anoNasc):
	from datetime import datetime
	anoNasc = abs(anoNasc)
	idade = datetime.today().year - anoNasc
	print(f'Com {idade} anos:',end=' ')
	
	if 65 >= idade >= 18:
		return 'VOTO OBRIGATÓRIO'
	elif  16 <= idade < 18 or idade > 65:
		return 'VOTO OPCIONAL'
	else:
		return 'NÃO VOTA'


print('=-='*20)
anoNasc = int(input('Digite seu ano de Nascimento:'))
print(voto(anoNasc))

