import math

co = float(input('digite o valor do Cateto oposto:'))
ca = float(input('digite o valor do Cateto adjacente:'))

h = math.sqrt(ca**2 + co**2)
h2 = math.hypot(co, ca)

print('A hipotenusa desse triangulo retangulo eh:{}'. format(h))
