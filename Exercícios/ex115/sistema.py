#from libs import interface         #Desse maneira está funcionando, teria apenas que alterar as chamadas das funções ( EX:arquivo.arquivoExiste
#from libs import arquivo           # e interface.menu() )

#import ex115                       #Dessa Maneira iria funcionar se o arquivo sistema.py estivesse na pasta Exercícios
#from ex115.libs import arquivo
#from ex115.libs import interface

from libs.arquivo import *          #Dessa Maneira iria funciona quando o arquivo sistema.py esta na pasta ex115
from libs.interface import *


#arq = 'cursoemvideo.txt'           #Será desse jeito quando abrirmos o folder na pasta ex115
arq = 'ex115\cursoemvideo.txt'      #Será desse jeito quando abrirmos o folder na pasta Exercício

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    op = menu(60)
    if op == '1':
        #Opção de Listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif op == '2':
        print('='*60)
        print('NOVO CADASTRO'.center(60))
        print('='*60)
        nome = str(input('Nome:')).strip().title()
        idade = int(input('Idade:'))
        cadastrar(arq,nome,idade)
    elif op == '3':
        print('Volte Sempre')
        break