temp = int(input('digite a quantidade de dias que o carro foi alugado:'))
rodado = float(input('digite a quantidade de Km que o carro percorreu:'))

print('O total a pagar eh:{:.2f} reais'. format(float(60*temp + 0.15*rodado)))