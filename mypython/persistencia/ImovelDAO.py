from mypython.persistencia.BancoDeDados import BancoDeDados
import mysql.connector

class ImovelDAO():
    def __init__(self):
        self.bd = BancoDeDados()


    #INSERT: Insere um novo imovel
    def insert(self, objImovel: object):
        try:
            #O Banco é Conectado
            bd = self.bd.conectar()
            print("Banco de Dados conectado...");

            #O cursor será preparado para executar os Comandos SQL
            cursor = bd.cursor()

            #Comando SQL
            add_imovel = "INSERT INTO tb_imovel(cd_imovel, nome, endereco, descricao, status_ , tipo, finalidade, " \
                         "nr_quarto, nr_sala, nr_banheiro, nr_vaga, cd_imobiliaria) " \
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            #Parametros do Comando SQL
            data_imovel = (objImovel.getId, objImovel.getNome, objImovel.getEndereco, objImovel.getDescricao,
                           objImovel.getStatus, objImovel.getTipo, objImovel.getFinalidade,
                           objImovel.getNumQuartos, objImovel.getNumSalas, objImovel.getNumBanheiros,
                           objImovel.getNumVagas, objImovel.getImobiliaria.getId)

            #Ordem para Execução do comando SQL, passado o camando SQL e os parametros
            cursor.execute(add_imovel, data_imovel)

            print("Imovel cadastrado com sucesso!")
        #Captura a exceção
        except mysql.connector.Error as err:
            print("Erro ao realizar o cadastro de Imovel. Erro:{}".format(err))

        #Executa após o try catch
        finally:
            response = self.bd.desconectar(bd, cursor)
            print(response)


    #DELETE: Deleta um imovel de acordo com o ID
    def delete(self, id_imovel: int):
        #Deleta imoveis relacionados
        try:
            #Instancia Banco de Dados e conecta ao banco
            bd = self.bd.conectar()
            print("Banco de dados conectado...")
            #Prepara o cursor
            cursor = bd.cursor()

            #Prepara comando SQL para excluir os imoveis realcionadas a imobiliaria
            delete = "delete from tb_imovel where cd_imovel = %s"
            delete_param = (id_imovel,)

            #executa o comando SQL
            cursor.execute(delete, delete_param)
            print("Imobiliaria Excluída com sucesso!")

        except mysql.connector.Error as err:
            print("Erro ao Excluir imoveis. Erro:{}".format(err))

        finally:
            response = self.bd.desconectar(bd, cursor)
            print(response)

    #UPDATE: Altera um registro de acordo com o ID
    def update(self, objImovel: object):
        try:
            #O Banco é Conectado
            bd = self.bd.conectar()
            print("Banco de dados conectado...")

            #O cursor será preparado para executar os Comandos SQL
            cursor = bd.cursor()

            #Comando SQL
            add_imovel = "update tb_imovel set nome = %s, endereco = %s, descricao = %s, status_ = %s, tipo = %s, " \
                        "finalidade = %s, nr_quarto = %s, nr_sala = %s, nr_banheiro = %s, nr_vaga = %s " \
                        "where cd_imovel = %s"

            #Parametros do Comando SQL
            data_imovel = (objImovel.getNome, objImovel.getEndereco, objImovel.getDescricao,
                           objImovel.getStatus, objImovel.getTipo, objImovel.getFinalidade,
                           objImovel.getNumQuartos, objImovel.getNumSalas, objImovel.getNumBanheiros,
                           objImovel.getNumVagas, objImovel.getId)

            #Ordem para Execução do comando SQL, passado o camando SQL e os parametros
            cursor.execute(add_imovel, data_imovel)

        #Captura a exceção
        except mysql.connector.Error as err:
            print("Erro ao realizar o update do Imovel.")

        #Executa após o try catch
        finally:
            response = self.bd.desconectar(bd, cursor)
            print(response)
    #SELECT
    #Selecionar todos os dados
    def selectAll(self):
        try:
            #O Banco é Conectado
            bd = self.bd.conectar()
            print("Banco de dados conectado...")

            #O cursor será preparado para executar os Comandos SQL
            cursor = bd.cursor()

            #Comando SQL
            add_imobi = "select * from tb_imovel"

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
    def selectNome(self, nome: str):
        try:
            #O Banco é Conectado
            bd = self.bd.conectar()
            print("Banco de dados conectado...")

            #O cursor será preparado para executar os Comandos SQL
            cursor = bd.cursor()

            #Comando SQL
            add_imovel = "select * from tb_imovel where nome like concat('%', %s, '%')"

            #Parametro para a Stored Procedure
            data_imovel = (nome,)

            #Ordem para Execução do comando SQL, passado o camando SQL e os parametros
            cursor.execute(add_imovel, data_imovel)

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