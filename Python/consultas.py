#Importando os resultados dos dados do código BD
from lib_database import *

#Importando biblioteca pythons System
import sys


# Função para trazer resultado de tipos de servidores, divididos pelos campus de atuação
def servidoresCampus(conexaoDB):
    print('\nConsultando tipos de servidores por campus')
    retorno = ServidoresCampusConsulta(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"\nCampus: {i[0]}\n Tipo: {i[1]}\n Quantidade: {i[2]}\n\n")
    else:
        print(retorno[0])
        sys.exit()


# Função para trazer resultado de docentes, divididos por disciplina de atuação
def docentesDisciplina(conexaoDB):
    print('\nConsultando docentes por disciplina')
    retorno = DocenteDisciplina(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"\nDocente: {i[0]}\n Disciplina: {i[1]}\n\n")
    else:
        print(retorno[0])
        sys.exit()

# Função para trazer resultado de quantidade de servidores por disciplinas
def DocentesPorDisciplinasECampus(conexaoDB):
    print('\nConsultando quantidade de docentes por disciplinas e por campus')
    retorno = DisciplinaCampus(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"\nDisciplina: {i[0]}\n Campus: {i[1]}\n Quantidade: {i[2]}\n\n")
    else:
        print(retorno[0])
        sys.exit()