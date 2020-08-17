x=int(input('digite um valor em metros da largura da parede:'))
y=int(input('digite um valor em metros da altura da parede:'))

print('Sabendo que cada litro de tinta equivale a 2 metros quadrado de parede então:')
print('será necessário {} litros de tinta'.format(x*y/2))