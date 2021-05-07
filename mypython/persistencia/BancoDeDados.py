#Classe responsavel por realizar conexão com o banco de dados

import mysql.connector



class BancoDeDados:
    def __init__(self):
        self.__conn = None
        self.__status = None

    def plugin(self):
        self.__conn = mysql.connector
        self.__status = "Obj pronto"

        return self.__conn

    def conectar(self):
        self.__conn = self.plugin()
        obj = self.__conn.connect(host='localhost', user='root', password='uniceub', database='bd_imobiliaria',
                                  autocommit=True)
        return obj

    def desconectar(self, bd, cursor):
        if bd.is_connected():
            cursor.close()
            bd.close()
            return "Banco de dados desconectado..."
        else:
            return "O Banco não foi conectado"