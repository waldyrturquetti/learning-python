import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site pudim com sucesso!\033[m')
    print(site.read()) 
    #Com isso conseguimos ter acesso ao código HTML do site (OBS: é "site" pois é o nome da variável que abrirmos o link do site pudim )