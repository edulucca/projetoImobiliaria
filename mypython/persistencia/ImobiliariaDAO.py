from mypython.persistencia.BancoDeDados import BancoDeDados
import mysql.connector

class ImobiliariaDAO():
    def __init__(self):
        self.bd = BancoDeDados()

    #INSERT: Insere uma nova imobiliaria
    def insert(self, objImobi: object):
        try:
            #O Banco é Conectado
            bd = self.bd.conectar()
            print("Banco de dados conectado...")

            #O cursor será preparado para executar os Comandos SQL
            cursor = bd.cursor()

            #Comando SQL
            add_imobi = "INSERT INTO tb_imobiliaria(cd_imobiliaria, nome, endereco) VALUES (%s, %s, %s)"

            #Parametros do Comando SQL
            data_imobi = (objImobi.getId, objImobi.getNome, objImobi.getEndereco)

            #Ordem para Execução do comando SQL, passado o camando SQL e os parametros
            cursor.execute(add_imobi, data_imobi)

        #Captura a exceção
        except mysql.connector.Error as err:
            print("Erro ao realizar o cadastro de imobiliaria.")

        #Executa após o try catch
        finally:
            response = self.bd.desconectar(bd, cursor)
            print(response)



    #DELETE: Deleta uma imobiliaria
    def delete(self, id_imobiliaria: int):
        #Deleta imoveis relacionados
        try:
            #Instancia Banco de Dados e conecta ao banco
            bd = self.bd.conectar()
            print("Banco de dados conectado...")

            #Prepara o cursor
            cursor = bd.cursor()

            #Prepara comando SQL para excluir os imoveis realcionadas a imobiliaria
            delete = "delete from tb_imovel where cd_imobiliaria = %s"
            delete_param = (id_imobiliaria,)

            #executa o comando SQL
            cursor.execute(delete, delete_param)
        except mysql.connector.Error as err:
            print("Erro ao Excluir imoveis. Erro:{}".format(err))

        finally:
            #Deleta Imobiliarias
            try:
                #Define comando SQL
                delete = "delete from tb_imobiliaria where cd_imobiliaria = %s"
                delete_param = (id_imobiliaria,)

                cursor.execute(delete, delete_param)
                print("Imobiliaria Excluída com sucesso!")

            except mysql.connector.Error as err:
                print("Erro ao Excluir Imobiliaria. Erro{}".format(err))

            finally:
                response = self.bd.desconectar(bd, cursor)
                print(response)



    #UPDATE: Atualiza um registro de a partir do codigo da Imobiliaria
    def update(self, objImobi: object):
        try:
            #O Banco é Conectado
            bd = self.bd.conectar()
            print("Banco de dados conectado...")

            #O cursor será preparado para executar os Comandos SQL
            cursor = bd.cursor()

            #Comando SQL
            add_imobi = "update tb_imobiliaria set nome = %s, endereco = %s where cd_imobiliaria = %s"

            #Parametros do Comando SQL
            data_imobi = (objImobi.getNome, objImobi.getEndereco, objImobi.getId)

            #Ordem para Execução do comando SQL, passado o camando SQL e os parametros
            cursor.execute(add_imobi, data_imobi)

        #Captura a exceção
        except mysql.connector.Error as err:
            print("Erro ao realizar o update de imobiliaria.")

        #Executa após o try catch
        finally:
            response = self.bd.desconectar(bd, cursor)
            print(response)


    #SELECT: Recupera os dados referentes as imobiliarias
    #Recupera todos os dados
    def selectAll(self):
        try:
            #O Banco é Conectado
            bd = self.bd.conectar()
            print("Banco de dados conectado...")

            #O cursor será preparado para executar os Comandos SQL
            cursor = bd.cursor()

            #Comando SQL
            add_imobi = "select * from tb_imobiliaria"

            #Ordem para Execução do comando SQL, passado o camando SQL e os parametros
            cursor.execute(add_imobi)

            #Captura as linhas consultadas e salva como uma lista
            result = cursor.fetchall()

            return result
        #Captura a exceção
        except mysql.connector.Error as err:
            print("Erro ao realizar a consulta de imobiliaria.")

        #Termina a execução do método
        finally:
            response = self.bd.desconectar(bd, cursor)
            print(response)

    #SELECT
    #Seleciona os dados de acordo com o informado e retorna os valores mais proximos do nome
    def selectNome(self, objImobi: object):
        try:
            #O Banco é Conectado
            bd = self.bd.conectar()
            print("Banco de dados conectado...")

            #O cursor será preparado para executar os Comandos SQL
            cursor = bd.cursor()

            #Comando SQL
            add_imobi = "select * from tb_imobiliaria where nome like concat('%', %s, '%')"

            #Parametro para a Stored Procedure
            data_imobi = (objImobi.getNome,)

            #Ordem para Execução do comando SQL, passado o camando SQL e os parametros
            cursor.execute(add_imobi, data_imobi)

            #Captura as linhas consultadas e salva como uma lista
            result = cursor.fetchall()

            return result
        #Captura a exceção
        except mysql.connector.Error as err:
            print("Erro ao realizar a consulta de imobiliaria. Erro {}:".format(err))

        #Termina a execução do método
        finally:
            response = self.bd.desconectar(bd, cursor)
            print(response)