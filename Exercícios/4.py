x=input('digite algo:')

print('O tipo dessa variável eh: {}'.format(type(x)))

print('É um número? {}'.format(x.isnumeric()))
print('É um alfabético? {}'.format(x.isalpha()))
print('É um alfanumérico? {}'.format(x.isalnum()))
print('É um está em minusculo? {}'.format(x.islower()))
print('É um está em maisculo? {}'.format(x.isupper()))
print('É um capitalizada? {}'.format(x.istitle()))