import urllib
import urllib.request

site = str(input('Insira o site: '))

try:
    site1 = urllib.request.urlopen('https://'+site+'/')
except urllib.request.URLError:
    print('O site não está acessível.')
else:
    print('O site está acessível.')
