
import aula22_Modulo

num = int(input('Digite um valor:'))
fat = aula22_Modulo.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {aula22_Modulo.dobro(num)}')
print(f'O triplo de {num} é {aula22_Modulo.triplo(num)}')

from aula22_Pacotes import numeros

num = int(input('Digite um valor:'))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')