# Importando o sys para nos ajudar com tratamento das funções
import sys

# Importando as funções e váriaveis do arquivo constantes.py
from constantes import *

# Função para ler o arquivo e indicado e separa-lo do seu cabeçalho.
# deixando apenas os dados puros para serem inseridos

def lerArquivo(nomeArquivo: str):
    lido = False
    dados_retorno = dict()
    try:
        arq_ = open(nomeArquivo, 'r', encoding=CODE_PAGE)
    except FileNotFoundError:
        dados_retorno = f'\nERRO: Arquivo Inexistente!'
    except:
        dados_retorno = f'\n ERRO: {sys.exc_info()[0]}'
    else:
        while True:
            linha = arq_.readline()[:-1]
            if not linha: break
            cabecalho =  linha.split(SEPARATOR)
            while True:
                linha = arq_.readline()[:-1]
                if not linha: break
                linha = linha.split(SEPARATOR)
                dados_retorno[linha[9]] = dict(zip(cabecalho, linha))
            lido = True
        arq_.close()
    finally:
        return lido, dados_retorno