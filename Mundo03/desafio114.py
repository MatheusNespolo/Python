import requests
import colorama

def verificar_site(url):
    try:
        resposta = requests.get({url}, timeout=5)
        if resposta.status_code == 200:
            print(f"O site {url} está acessível!")
        else:
            print(f"O site {url} retornou o código de status {resposta.status_code}.")
    except requests.ConnectionError:
        print(colorama.Back.RED + f"Não foi possível conectar ao site {url}." + colorama.Style.RESET_ALL)
    except requests.Timeout:
        print(colorama.Back.RED + f"O tempo de conexão com o site {url} expirou." + colorama.Style.RESET_ALL)
    except Exception as e:
        print(colorama.Back.RED + f"Ocorreu um erro ao verificar o site {url}: {e}" + colorama.Style.RESET_ALL)

# Teste
verificar_site("https://www.pudim.com.br")
