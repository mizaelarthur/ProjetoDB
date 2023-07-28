# Importando as funções e váriaveis do arquivo lib_database, que trata das conexões com o BD
from lib_database import *
# Importando a biblioteca sys para nos auxiliar
import sys

# ===================================================================================================
# Logo Abaixo iremos criar 3 consultas. em uma iremos consultar os tipos de servidores, na outra
# os docentes por disciplina e na ultima a quantidade de doscentes por disciplina e campus. 
# As funções iram acionar as funções do arquivo lib.database que fará a ponte entre o BD e o arquivo
# ===================================================================================================


# Definindo a váriavel que será solicitada no arquivo SETUP.py
def consultaSC(conexaoDB):
    print('\nConsultando tipos de servidores por campus\n')
    retorno = consultaServCampus(conexaoDB) # Enviando a requisição atraves da função definida em lib_database
    if retorno[0] == True:
        # Usaremos um for para ir exibindo o resultado recebido linha por linha
        for i in retorno[1]:
            print(f"\nCampus: {i[0]:5} \nTipo de servidor: {i[1]:<25} \nQuantidade: {i[2]:<1}\n")
    else:
        print(retorno[0])
        sys.exit()

# Definindo a váriavel que será solicitada no arquivo SETUP.py
def consultaDD(conexaoDB):
    print('\nConsultando docentes por disciplina\n')
    retorno = consultaDocenteDisc(conexaoDB) # Enviando a requisição atraves da função definida em lib_database
    if retorno[0] == True:
        # Usaremos um for para ir exibindo o resultado recebido linha por linha
        for i in retorno[1]:
            print(f"\nDocente: {i[0]:<45} \nDisciplina: {i[1]}\n\n")
    else:
        print(retorno[0])
        sys.exit()

# Definindo a váriavel que será solicitada no arquivo SETUP.py
def qtdDDC(conexaoDB):
    print('\nConsultando quantidade de docentes por disciplinas e por campus\n')
    retorno = consultaDiscCampi(conexaoDB) # Enviando a requisição atraves da função definida em lib_database
    if retorno[0] == True:
        for i in retorno[1]:
            # Usaremos um for para ir exibindo o resultado recebido linha por linha
            print(f"\nDisciplina: {i[0]:<60} \nCampus: {i[1]:<5} \nQuantidade: {i[2]:<1}\n\n")
    else:
        print(retorno[0])
        sys.exit()