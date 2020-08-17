
def area(l, c):
	area = l*c
	print(f'A área do terreno eh {l:.2f} x {c:.2f} é de {area:.2f} m^2.')


print(' Controle de Terrenos')
print('=='*20)

largura = float(input('Digite a LARGURA:'))
comprimento = float(input('Digite o COMPRIMENTO:'))

area(comprimento, largura)

