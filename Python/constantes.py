# Importando a Biblioteca "os" para ajudar a obter o caminho do nosso diretório
import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Tipo de codificação de linguagem para Portugues Brasil
CODE_PAGE = "utf-8"

# Definindo item separador de colunas no nosso arquivo dados.csv
SEPARATOR = ";"