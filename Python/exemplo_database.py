import sys
from lib_exemplo import *
from lib_database import *
from constantes import *
from configBD import *

def inserirDados():
    retLeitura  = lerArquivo(APP_DIR + '\\DadosBrutos.csv')

    if not retLeitura[0]:
        print(retLeitura[1])
        sys.exit()

    print('\nTratando os dados lidos')
    dados_lidos = retLeitura[1]

    setCategoria                = set(map(lambda c: c['categoria'], dados_lidos.values()))
    setCargo                    = set(map(lambda c: c['cargo'], dados_lidos.values()))
    setSetorSiape               = set(map(lambda c: c['setor_siape'], dados_lidos.values()))
    setDisciplinaIngresso       = set(map(lambda c: c['disciplina_ingresso'], dados_lidos.values()))
    setSetorSuap                = set(map(lambda c: c['setor_suap'], dados_lidos.values()))
    setFuncao                   = set(map(lambda c: c['funcao'], dados_lidos.values()))
    setJornadaTrabalho          = set(map(lambda c: c['jornada_trabalho'], dados_lidos.values()))
    setCampus                   = set(map(lambda c: c['campus'], dados_lidos.values()))

    retConexao = conectaDB(DB_HOST, DB_NAME, DB_USER, DB_PASS)


    if not retConexao[0]:
        print(retConexao[1])
        sys.exit()


    connDB = retConexao[1]

    print('\nInserindo dados na tabela SETOR_SIAPE')
    dictSetorSiape = dict()
    for setorSiape in setSetorSiape:
        if not setorSiape: setorSiape = '------'
        retorno = insereSiape(setorSiape, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictSetorSiape[setorSiape] = retorno[1]

    print('\nInserindo dados na tabela CARGO')
    dictCargo = dict()
    for cargo in setCargo:
        if not cargo: cargo = '------'
        retorno = insereCargo(cargo, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictCargo[cargo] = retorno[1]


    print('\nInserindo dados na tabela SETOR_SIAPE')
    dictSetorSiape = dict()
    for setorSiape in setSetorSiape:
        if not setorSiape: setorSiape = '------'
        retorno = insereSiape(setorSiape, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictSetorSiape[setorSiape] = retorno[1]


    print('\nInserindo dados na tabela DISCIPLINA_INGRESSO')
    dictDisciplinaIngresso = dict()
    for disciplinaIngresso in setDisciplinaIngresso:
        if not disciplinaIngresso: disciplinaIngresso = '------'
        retorno = insereDisciplina(disciplinaIngresso, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictDisciplinaIngresso[disciplinaIngresso] = retorno[1]

    print('\nInserindo dados na tabela CATEGORIA')
    dictCategoria = dict()
    for categoria in setCategoria:
        if not categoria: categoria = '------'
        retorno = insereCategoria(categoria, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictCategoria[categoria] = retorno[1]
    

    print('\nInserindo dados na tabela SETOR_SUAP')
    dictSetorSuap = dict()
    for setorSuap in setSetorSuap:
        if not setorSuap: setorSuap = '------'
        retorno = insereSuap(setorSuap, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictSetorSuap[setorSuap] = retorno[1]

    print('\nInserindo dados na tabela FUNCAO')
    dictFuncao = dict()
    for funcao in setFuncao:
        if not funcao: funcao  = '------'
        retorno = insereFuncao(funcao, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictFuncao[funcao] = retorno[1]

    print('\nInserindo dados na tabela JORNADA_TRABALHO')
    dictJornadaTrabalho = dict()
    for jornadaTrabalho in setJornadaTrabalho:
        if not jornadaTrabalho: jornadaTrabalho = '------'
        retorno = insereJornada(jornadaTrabalho, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictJornadaTrabalho[jornadaTrabalho] = retorno[1]

    print('\nInserindo dados na tabela CAMPUS')
    dictCampus = dict()
    for campus in setCampus:
        if not campus: campus = '------'
        retorno = insereCampus(campus, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictCampus[campus] = retorno[1]

    print('\nInserindo dados na tabela SERVIDOR')
    tupleCampos = tuple(['categoria'         ,   'cargo'      ,  'setor'       ,
                        'disciplina'        ,   'setor_suap' ,  'nome'           ,
                        'funcao'            ,   'jornada_trabalho'    ,  'telefones'   ,
                        'matricula'   ,   'curriculo_lattes'     ,  'campus'      ,   
                        'url_foto_75x100'])





    retorno = insereServidor(tupleCampos, 0, connDB)

    if not retorno[0]: print(retorno[1])
#ENCERRA A CONEXÃO COM O BANCO
    connDB.close()