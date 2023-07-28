
from lib_database import *

import sys


def consultaSC(conexaoDB):
    print('\nConsultando tipos de servidores por campus\n')
    retorno = consultaServCampus(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"Campus: {i[0]:5} Tipo de servidor: {i[1]:<25} Quantidade: {i[2]:<1}")
    else:
        print(retorno[0])
        sys.exit()


def consultaDD(conexaoDB):
    print('\nConsultando docentes por disciplina\n')
    retorno = consultaDocenteDisc(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"Docente: {i[0]:<45} Disciplina: {i[1]}")
    else:
        print(retorno[0])
        sys.exit()


def qtdDDC(conexaoDB):
    print('\nConsultando quantidade de docentes por disciplinas e por campus\n')
    retorno = consultaDiscCampi(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"Disciplina: {i[0]:<60} Campus: {i[1]:<5} Quantidade: {i[2]:<1}")
    else:
        print(retorno[0])
        sys.exit()