frase = 'Curso em Vídeo Python'

print(frase[9])
print(frase[9:13])
print(frase[9:21:2]) #pula de 2 em 2

print(frase[0:5]) #equivalente a [0:5]
print(frase[15:]) #eqivalente a [15:21]

print(frase[9::3])


print(len(frase)) #comprimento da string
print(frase.count('o')) #conta quantas vezes vezes o caracter 'o' aparece
print(frase.count('o',0,13)) #conta quantas vezes vezes o caracter 'o' aparece do indice 0 ao 12

print(frase.find('deo')) #Em que indice ele encontou 'deo' na string //find = encontrar

print(frase.find('Android')) #retorna -1

print('Curso' in frase) 

print(frase.replace('Python','Android')) #Substitui a string python por android, mas não de forma permanente
print(frase)

print(frase.upper()) #Coloca tudo em maiusculo
print(frase.lower()) #Coloca tudo em minisculo
print(frase.capitalize()) # coloca a primeira letra em maiusculo e o resto da string passa em minusculo 
print(frase.title()) #funciona parecido com o capitalize, porém é com todos as 
					#palavras(todo serie de caracteres que começar depois do space) da string  

frase1 = '   Aprenda Python  '
print(frase1)
print(frase1.strip()) #Tira os spaces desnecessários, ou seja os do inicio e final
print(frase1.rstrip()) #Tira os spaces desnecessários da direita, ou seja do final
print(frase1.lstrip()) #Tira os spaces desnecessários da esquerda, ou seja do inicio

print(frase.split()) #divide a string e coloca cada palavra em uma posição de um lista
print('-'.join(frase.split()))
print('-'.join(frase))

print("""sadasd,sa,dãs,da,dsaç,dsa,dã,sdasç,ad,ãs,dçsdlskkmcskmcpmcm
sadmaskmdkasmdlkmasdmasdkmalskmlaknfknaklnlakslkmsxmalskmxlmaksmx
sxasxaslkmxlakmsxlakmsxlakmxlakmxlakmxlakmxlasmxlakmxlasmxlamx""")

print(frase.lower().find('vídeo'))



