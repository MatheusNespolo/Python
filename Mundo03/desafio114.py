import requests
import colorama

def verificar_site(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f"O site {url} está acessível!")
        else:
            print(f"O site {url} retornou o código de status {resposta.status_code}.")
    except requests.ConnectionError:
        print(f"Não foi possível conectar ao site {url}.")
    except requests.Timeout:
        print(f"A conexão com o site {url} expirou.")
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o site {url}: {e}")

# Teste
verificar_site("https://www.pudim.com.br")
