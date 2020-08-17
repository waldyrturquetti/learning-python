import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobra(valor)}')
print(f'Aumentando 10% de {valor} temos {moeda.aumentar(valor,10)}')
print(f'diminuindo 10% de {valor} temos {moeda.diminuir(valor,10)}')
