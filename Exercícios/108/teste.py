import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobra(valor))}')
print(f'Aumentando 10% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.aumentar(valor,10))}')
print(f'diminuindo 10% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.diminuir(valor,10))}')
