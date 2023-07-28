import psycopg2, sys
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
    

def insertCargo(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO cargo (cargo) VALUES (\'{descricao}\') RETURNING id_cargo;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    

def insertCampus(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO campus (campus) VALUES (\'{descricao}\') RETURNING id_campus;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    


def insertJornada(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO jornada_trabalho (jornada) VALUES (\'{descricao}\') RETURNING id_jornada;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    


def insertSiape(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO setor_siape (setor_siape) VALUES (\'{descricao}\') RETURNING id_setor;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    
    

def insertSuap(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO setor_suap (setor_suap) VALUES (\'{descricao}\') RETURNING id_setor_suap;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    


def insertDisciplina(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO disciplina_ingresso (disciplina) VALUES (\'{descricao}\') RETURNING id_disciplina;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    

def insertFuncao(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO funcao (funcao) VALUES (\'{descricao}\') RETURNING id_funcao;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    
    


def insertCategoria(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO categoria (categoria) VALUES (\'{descricao}\') RETURNING id_categoria;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    
    

def insertServidor(campos: tuple, valores: tuple, conexao):
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
    






    # =========== CONSULTAS ==============
def ServidoresCampus(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM servidorescampus ORDER BY sigla;'
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



def DocenteDisciplina(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM docentesdisciplinas;'
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


def DisciplinaCampus(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM disciplinascampus ORDER BY sigla;'
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
