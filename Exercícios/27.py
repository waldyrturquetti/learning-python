nome = str(input('Digite o nome completo:')).strip()
#print(nome)

nome = nome.split()
#print(nome)

#print(len(nome))

print('Primeiro:{}'.format(nome[0]))
print('Último:{}'.format(nome[ len(nome) - 1 ]))