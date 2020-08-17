#Ordem de Precedência:
#()
#**  (Elevação)
#* / //(divisão inteira) %(resto)
# + -

print('oi'+'olá')
print('oi'*5)

nome  = input('digite seu nome:')
print('Prazer em te conhecer {:20}!!!'.format(nome))
print('Prazer em te conhecer {:>20}!!!'.format(nome))
print('Prazer em te conhecer {:<20}!!!'.format(nome))
print('Prazer em te conhecer {:^20}!!!'.format(nome))
print('Prazer em te conhecer {:=^20}!!!'.format(nome))

n1  = int(input('digite um valor:'))
n2  = int(input('digite outro valor:'))

print('a soma eh:{}, a multiplicação eh:{}'.format(n1+n2,n1*n2), end=' o caraiooooo') #o end substitui o \n que é default no print
print('A Elevação eh:{}\nE a divisão inteira eh:{}'.format(n1**n2, n1//n2))

