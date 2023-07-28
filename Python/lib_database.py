#Importa as bibliotecas necessarias para fazer a conexão com o banco e as bibliotecas do sistema
import psycopg2, sys

#Abre a conexão de fato com o banco
def conectaDB(server: str, database: str, dbuser: str, userpwd: str):
    conectado = False
    conexao = None
    try:
        conexao =  psycopg2.connect(f'dbname={database} user={dbuser} host={server} password={userpwd}')
    except:
        conexao = f'ERRO: {sys.exc_info()[0]}'
    else:
        conectado = True
    finally:
        return conectado, conexao
    
def inserirCargo(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO cargo (ncargo) VALUES (\'{descricao}\') RETURNING id_cargo;'
    
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT ncargo FROM cargo WHERE ncargo = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    
def inserirCampus(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO campus (ncampus) VALUES (\'{descricao}\') RETURNING id_campus;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT ncampus FROM campus WHERE ncampus = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CAMPUS): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

def inserirJornada(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO jornada_trabalho (jornada) VALUES (\'{descricao}\') RETURNING id_jornada;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT jornada FROM jornada_trabalho WHERE jornada = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela JORNADA_TRABALHO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

def inserirSiape(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO setor_siape (nsetor) VALUES (\'{descricao}\') RETURNING id_setor;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT setor_siape FROM setor_siape WHERE setor_siape = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela SETOR_SIAPE): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    
def inserirSuap(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO setor_suap (nsetor_suap) VALUES (\'{descricao}\') RETURNING id_setor_suap;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nsetor_suap FROM setor_suap WHERE nsetor_suap = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela SETOR_SUAP): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

def inserirDisciplina(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO disciplina_ingresso (ndisciplina) VALUES (\'{descricao}\') RETURNING id_disciplina;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT ndisciplina FROM disciplina_ingresso WHERE ndisciplina = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela DISCIPLINA_INGRESSO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

def inserirFuncao(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO funcao (nfuncao) VALUES (\'{descricao}\') RETURNING id_funcao;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nfuncao FROM funcao WHERE nfuncao = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela FUNCAO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    

def inserirCategoria(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO categoria (ncategoria) VALUES (\'{descricao}\') RETURNING id_categoria;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT ncategoria FROM categoria WHERE ncategoria = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CATEGORIA): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    
def inserirServidor(campos: tuple, valores: tuple, conexao):
    inserido = False
    idRetorno = None
    strSQL = 'INSERT INTO servidor ('
    for i in campos:    strSQL += i + ', '
    strSQL = strSQL[:-2]
    strSQL += f') VALUES {valores} RETURNING matricula_servidor;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n{valores}\n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

def consultaServCampus(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM consultas_servidores_campus ORDER BY sigla;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n'
    else:
        consultado = True
        idRetorno = cursorTable.fetchall()
        conexao.commit()
    finally:
        return consultado, idRetorno


def consultaDiscCampi(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM consultas_disciplinas_campus ORDER BY sigla;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n'
    else:
        consultado = True
        idRetorno = cursorTable.fetchall()
        conexao.commit()
    finally:
        return consultado, idRetorno
    
def consultaDocenteDisc(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM consultas_docentes_disciplinas;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n'
    else:
        consultado = True
        idRetorno = cursorTable.fetchall()
        conexao.commit()
    finally:
        return consultado, idRetorno
    