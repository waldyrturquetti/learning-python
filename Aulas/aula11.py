'''
PADRÃO ANSI

Style(estilo):					text:					back(fundo):são as mesmas cores para o texto e na mesma ordem
0-none(nenhum)					30:branco				40:
1-bold(negrito)					31:vermelho				41:
4-underline(sublinhado)			32:verde				42:
7-negative						33:amarelo				43:
								34:azul					44:
								35:magena(roxo)			45:
								36:cianta(verde água)	46:
								37:cinza				47:

Cod Exemplo: 	\033[0;33;44m

'''

print('\033[1;31;43mOlá, Mundo\033[m')
print('\033[4;30;45mOlá, Mundo\033[m')
print('\033[7;33;44mOlá, Mundo\033[m')#inverte, se seria letra amarela e fundo azul, será letra azul e fundo amarelo
print('\033[4;30;41mOlá, Mundo\033[m')

a=3
b=2
print('Os valores são \033[32m{}\033[m e \033[33m{}\033[m !!!!'.format(a,b))

#OU

nome = 'Waldyr'

print('Olá, muito prazer {}{}{}'.format('\033[35;46m' ,nome, '\033[m'))

#OU

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m',}
print('Olá, muito prazer {}{}{}'.format(cores['amarelo'] ,nome, cores['limpa']))
print('Olá, muito prazer {}{}{}'.format(cores['pretoebranco'] ,nome, cores['limpa']))