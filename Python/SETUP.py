#importa as bibliotecas e arquivos necessários
import sys
from conexao_db import *
from lib_exemplo import *
from exemplo_database import *
from consultas import *

def main():
    retConexao = conectaDB(DB_HOST, DB_NAME, DB_USER, DB_PASS)

    if not retConexao[0]:
        print(retConexao[1])
        sys.exit()

    connDB = retConexao[1]
    while True:
        print('\n=====================================================================================================\n')
        print('Olá, seja bem-vindo ao nosso SETUP. esse é um ambiente mais amigável para escolhas.')
        print('\nDeseja realizar uma consulta ou cadastro?  (para sair, digite a palavra "sair")')
        escolha = input()

        if escolha == 'sair':
            print("Foi um prazer, até mais!")
            connDB.close()
            sys.exit()
        elif escolha == 'cadastro':
            inserir()
        elif escolha == 'consulta':
            print("1. Quantidade de docentes por disciplinas e por campus.")
            print("2. Docentes por disciplina.")
            print("3. Tipos de servidores por campus.")
            new_escolha = input('Qual das consultas você deseja? (Digite um número)')
            if new_escolha == '1':
                qtdDDC(connDB)
            elif new_escolha == '2':
                consultaDD(connDB)
            elif new_escolha == '3':
                consultaSC(connDB)
            else:
                print('Opção Invalida!')
            
        else:
            print("\nOPÇÃO INVÁLIDA!!!\n")

if __name__ == "__main__":
    main()