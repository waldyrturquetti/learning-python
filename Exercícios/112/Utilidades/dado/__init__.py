
def verifica(valor):
	veriAntes = False
	veriDepois = False
	count = 0
	
	#print(valor)
	num=str(valor).strip("[]")
	#print(num)
	
	for c in num[1:-1]:
		if c.isnumeric() is False and c not in '.,':
			#print(c)
			#print(c.isnumeric())
			#print(1)
			return False
		if c.isdecimal() is True:
			if count == 0:
				veriAntes = True
			else:
				veriDepois = True
		elif c in '.,':
			count += 1
			if veriAntes is False or count > 1:
				#print(2)
				return False
	
	if veriAntes is True:	
		if veriDepois is False and count == 0:
			#print(3)
			return True
		elif veriDepois is True and count == 1:
			#print(4)
			return True
		else:
			#print(5)
			return False
	else:
		#print(6)
		return False


def passaFlaot(valor):
	num=str(valor).strip("[]")[1:-1]
	num=num.replace(",",".")
	print(num)
	num2 = float(num)
	return num2


'''
Poderia ser feito apenas essa função tbm
def leiaDinhiro(msg):
	valido = false
	entrada = str(input(msg)).replace(',','.').strip()
	if entrada.isalpha() or entrada == ''
		print(f'\033[31mERRO!!"{valor}" é um preço inválido\033[m')
	else:
		valido = True
		return float(entrada) 
'''