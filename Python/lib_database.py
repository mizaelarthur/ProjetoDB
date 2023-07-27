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
    
#Insere de fato os dados na tabela CARGO    
def insereCargo(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO cargo (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM cargo WHERE nome = \'{descricao}\';'
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
    
#Insere de fato os dados na tabela CAMPUS
def insereCampus(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO campus (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM campus WHERE nome = \'{descricao}\';'
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

#Insere de fato os dados na tabela JORNADA_TRABALHO
def insereJornada(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO jornada_trabalho (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM jornada_trabalho WHERE nome = \'{descricao}\';'
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

#Insere de fato os dados na tabela SETOR_SIAPE
def insereSiape(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO setor_siape (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM setor_siape WHERE nome = \'{descricao}\';'
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
    
#Insere de fato os dados na tabela SETOR_SUAP
def insereSuap(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO setor_suap (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM setor_suap WHERE nome = \'{descricao}\';'
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

#Insere de fato os dados na tabela DISCIPLINA_INGRESSO
def insereDisciplina(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO disciplina_ingresso (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM disciplina_ingresso WHERE nome = \'{descricao}\';'
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

#Insere de fato os dados na tabela FUNCAO
def insereFuncao(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO funcao (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM funcao WHERE nome = \'{descricao}\';'
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
    

#Insere de fato os dados na tabela CATEGORIA
def insereCategoria(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO categoria (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM categoria WHERE nome = \'{descricao}\';'
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
    
    
#Insere de fato os dados na tabela SERVIDOR
def insereServidor(campos: tuple, valores: tuple, conexao):
    inserido = False
    idRetorno = None
    strSQL = 'INSERT INTO servidor ('
    for i in campos:    strSQL += i + ', '
    strSQL = strSQL[:-2]
    strSQL += f') VALUES {valores} RETURNING matricula;'
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
    
#Faz a consulta do tipo de servidores por campus
def consultaServidoresCampus(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM servidores_campus ORDER BY sigla;'
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

#Faz a consulta de todos os docentes por disciplina
def consultaDocenteDisciplina(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM docentes_disciplinas;'
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
  
#Faz a consulta da quantidade de docentes por disciplina e por campus    
def consultaDisciplinaCampus(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM disciplinas_campus ORDER BY sigla;'
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