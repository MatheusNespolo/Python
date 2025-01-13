from urllib import request, error

# Verificar se um site está acessível
try:
    site = request.urlopen("http://www.pudim.com.br/")
except error.URLError:
    print("O site não está acessível nesse momento...")
else:
    print("O site com acesso...!")
