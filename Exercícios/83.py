import string

alfabeto = list(string.ascii_lowercase)
listaNumeros = ['1','2','3','4','5','6','7','8','9','0']
alfabeto = alfabeto + listaNumeros
operadores = ['*','/','+','-']

count_1 = 0
flag = True

lista = list(str(input('Digite uma expressão:')).replace(" ",""))
print(lista)
aux = len(lista) - 1

if lista[0] in operadores and lista[aux] in operadores:
	print('expressão inváilida')
	flag = False
elif '+' not in lista and '-' not in lista and '*' not in lista and '/' not in lista:
	print('expressão inváilida')
	print(0)
	flag = False
else:
	for c in range(len(lista)):
		if lista[c] == '(':
			count_1 += 1
			if c == 1:
				if lista[c - 1] in operadores:
					print('expressão inváilida')
					print(c)
					flag = False
					print(1)
					break
			elif c > 1:
				if lista[c - 1] not in operadores:
					print('expressão inváilida')
					flag = False
					print(c)
					print(2)
					break

			if lista[c + 1] in operadores:
				print('expressão inválida')
				flag = False
				print(c)
				print(3)
				break

			aux = lista[c + 1]
			if aux.lower() not in alfabeto:
				print('expressão inváilida')
				flag = False
				print(c)
				print(4)
				break

		elif lista[c] == ')':
			count_1 -= 1
			if c  == len(lista) - 2:
				if lista[c + 1] in operadores:
					print('expressão inváilida')
					flag = False
					print(c)
					print(5)
					break

			elif c < len(lista) - 2:
				if lista[c + 1] not in operadores:
					print('expressão inváilida')
					flag = False
					print(c)
					print(6)
					break

			aux = lista[c - 1]
			if aux.lower() not in alfabeto:
				print('expressão inváilida')
				flag = False
				print(c)
				print(7)
				break

		
'''		
if lista[c - 1] != '+' or lista[c - 1] != '-' or lista[c - 1] != '*' or lista[c - 1] != '/':
				print('expressão inváilida')
				flag = False
				break
'''

if flag is True and count_1 == 0:
	print('expressão válida')


#(a+b)+(a+(r+t)*i)*(c)