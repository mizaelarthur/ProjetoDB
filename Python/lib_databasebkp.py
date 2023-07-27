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
    strSQL = f'INSERT INTO Cargo (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM Cargo WHERE nome = \'{descricao}\';'
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
    strSQL = f'INSERT INTO Campus (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM Campus WHERE nome = \'{descricao}\';'
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
    strSQL = f'INSERT INTO Jornada_Trabalho (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM Jornada_Trabalho WHERE nome = \'{descricao}\';'
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
    strSQL = f'INSERT INTO Setor_siape (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM Setor_siape WHERE nome = \'{descricao}\';'
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
    strSQL = f'INSERT INTO Setor_suap (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM Setor_suap WHERE nome = \'{descricao}\';'
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
    strSQL = f'INSERT INTO Disciplina_ingresso (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM Disciplina_ingresso WHERE nome = \'{descricao}\';'
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
    strSQL = f'INSERT INTO Funcao (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM Funcao WHERE nome = \'{descricao}\';'
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
    strSQL = f'INSERT INTO Categoria (nome) VALUES (\'{descricao}\') RETURNING id;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome FROM Categoria WHERE nome = \'{descricao}\';'
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