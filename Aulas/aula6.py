x= int(input('Digite o numero 1:'))
y= int(input('Digite o numero 2:'))

s=x+y;
#print('A soma vale {}'.format(s))
print('A soma de {} e de {} eh:{}'.format(x,y,s))

print(type(x))
print(type('hello'))

n=input('digite um algo:')
print(type(n)) #tipo de n
print(n.isdecimal()) #apenas numeros 
print(n.isalnum()) #se possui numeros ou letras
print(n.isalpha()) #apenas letras
print(n.isascii()) #se está na tabela ascii
print(n.isdigit()) #se é completamente composta por numeros
print(n.isidentifier()) #se todos os caracteres são válidos para escrever um identificador no código
print(n.islower()) #se todas as letras são minisculas 
print(n.isnumeric()) #se é numérico
print(n.isprintable()) #se é possível printar na tela
print(n.isspace()) #se é um space(espaço)
print(n.istitle()) # para detectar as palavras estão escritas string é uma primeira letra maiúscula e outras letras em minúsculas.
print(n.isupper()) #se todas as letras são maiusculas
