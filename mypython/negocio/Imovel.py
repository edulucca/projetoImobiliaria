from mypython.negocio.Imobiliaria import Imobiliaria
from mypython.persistencia.ImovelDAO import ImovelDAO


class Imovel(Imobiliaria):
    # Construtor Cheio
    def __init__(self, imobiliaria: Imobiliaria = "", id=0, nome="", endereco="", descricao="", status="", tipo="", finalidade="",
                 numQuartos=0, numSalas=0, numBanheiros=0, numVagas=0):
        self.__imobiliaria = imobiliaria
        self.__id = id
        self.__nome = nome
        self.__endereco = endereco
        self.__descricao = descricao
        self.__status = status
        self.__tipo = tipo
        self.__finalidade = finalidade
        self.__numQuartos = numQuartos
        self.__numSalas = numSalas
        self.__numBanheiros = numBanheiros
        self.__numVagas = numVagas

    # Metodo Get/Set da classe
    @property
    def getImobiliaria(self):
        return self.__imobiliaria

    def setImobiliaria(self, imobiliaria:Imobiliaria):
        self.__imobiliaria = imobiliaria

    @property
    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    @property
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    @property
    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco = endereco

    @property
    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, descricao):
        self.__descricao = descricao


    @property
    def getStatus(self):
        return self.__status


    def setStatus(self, status):
        self.__status = status


    @property
    def getTipo(self):
        return self.__tipo


    def setTipo(self, tipo):
        self.__tipo = tipo


    @property
    def getFinalidade(self):
        return self.__finalidade


    def setFinalidade(self, finalidade):
        self.__finalidade = finalidade


    @property
    def getNumQuartos(self):
        return self.__numQuartos

    def setNumQuartos(self, numQuartos):
        self.__numQuartos = numQuartos

    @property
    def getNumSalas(self):
        return self.__numSalas

    def setNumSalas(self, numSalas):
        self.__numSalas = numSalas

    @property
    def getNumBanheiros(self):
        return self.__numBanheiros

    def setNumBanheiros(self, numBanheiros):
        self.__numBanheiros = numBanheiros

    @property
    def getNumVagas(self):
        return self.__numVagas

    def setNumVagas(self, numVagas):
        self.__numVagas = numVagas

    # Métodos de Persistencia da Classe
    # Cadastrar Imovel
    def cadastrar(self):
        try:
            # Garante que um ID igual a outro, não seja gravado
            validar = ImovelDAO().selectAll()

            for i in validar:
                if i[0] == self.__id:
                    return "ID do Imovel já foi cadastrado! Tente outro, por favor."

            # Valida o campo Nome*
            if self.__nome == "":
                return "Nome não foi inserido! Tente novamente!"

            ImovelDAO().insert(self)
            return "Imovel cadastrado com sucesso!"

        except Exception as err:
            return "Erro ao cadastrar Imovel!"

    # Excluir Imovel
    def excluir(self, id: int):
        try:
            ImovelDAO().delete(id)
            return "Imovel excluida com sucesso!"
        except:
            return "Erro ao excluir Imovel!"

    # Alterar os dados de um imovel a partir da ID
    def alterar(self):
        try:
            ImovelDAO().update(self)
            return "Imovel atualizada com sucesso!"
        except:
            return "Erro ao atualizar Imovel!"

    # Consulta todos os dados de imoveis e salva em uma lista
    def recuperarTodos(self):
        try:
            # Recuperar os dados do Banco de Dados
            dados = ImovelDAO().selectAll()

            # Algoritimo para add os dados recperados em um dicionario com indexação
            jsonRetorno = dict()
            contador = 1
            for i in dados:

                if i[4] == 'A':
                    status = "ATIVO"
                else:
                    status = "INATIVO"

                if i[5] == 'C':
                    tipo = "CASA"
                elif i[5] == 'A':
                    tipo = "APARTAMENTO"
                else:
                    tipo = "INDEFINIDO"

                if i[6] == 'R':
                    fim = "RESIDENCIAL"
                elif i[6] == 'E':
                    fim = "ESCRITORIO"
                else:
                    fim = "INDEFINIDO"

                jsonRetorno.setdefault((contador), []).append({
                    'Código da Imobiliaria': i[11],
                    'Codigo do Imovel': i[0],
                    'Nome do Imovel': i[1],
                    'Endereço': i[2],
                    'Descrição': i[3],
                    'Status': status,
                    'Tipo': tipo,
                    'Finalidade': fim,
                    'Número de Quartos': i[7],
                    'Número de Salas': i[8],
                    'Número de Banheiros': i[9],
                    'Número de Vagas': i[10]
                })
                contador = contador + 1
            return jsonRetorno
        except:
            return "Erro ao recuperar dados!"

    # Consulta Inteligente de acordo com o Nome
    def recuperarNomeFiltro(self, nome: str):
        try:
            # Recuperar os dados do Banco de Dados
            dados = ImovelDAO().selectNome(nome)
            # Algoritimo para add os dados recperados em um dicionario com indexação
            jsonRetorno = dict()
            contador = 1
            for i in dados:
                if i[4] == 'A':
                    status = "ATIVO"
                else:
                    status = "INATIVO"

                if i[5] == 'C':
                    tipo = "CASA"
                elif i[5] == 'A':
                    tipo = "APARTAMENTO"
                else:
                    tipo = "INDEFINIDO"

                if i[6] == 'R':
                    fim = "RESIDENCIAL"
                elif i[6] == 'E':
                    fim = "ESCRITORIO"
                else:
                    fim = "INDEFINIDO"

                jsonRetorno.setdefault((contador), []).append({
                    'Código da Imobiliaria': i[11],
                    'Codigo do Imovel': i[0],
                    'Nome do Imovel': i[1],
                    'Endereço': i[2],
                    'Descrição': i[3],
                    'Status': status,
                    'Tipo': tipo,
                    'Finalidade': fim,
                    'Número de Quartos': i[7],
                    'Número de Salas': i[8],
                    'Número de Banheiros': i[9],
                    'Número de Vagas': i[10]
                })
                contador = contador + 1
            return jsonRetorno
        except:
            return "Erro ao recuperar dados!"


    def recuperarTodosPage(self, inicio: int, final: int):
        try:
            # Declaração de Variaveis
            dados = []
            cursor = inicio - 1
            jsonRetorno = dict()
            #Recuperar os dados do Banco de Dados
            consulta = ImovelDAO().selectAll()

            #Seleciona os dados pedidos e adiciona em nova lista
            for i in range(inicio, final + 1):
                dados.append(consulta[cursor])
                cursor = cursor + 1

            #Algoritimo para add os dados recperados em um dicionario com indexação
            for i in dados:

                if i[4] == 'A':
                    status = "ATIVO"
                else:
                    status = "INATIVO"

                if i[5] == 'C':
                    tipo = "CASA"
                elif i[5] == 'A':
                    tipo = "APARTAMENTO"
                else:
                    tipo = "INDEFINIDO"

                if i[6] == 'R':
                    fim = "RESIDENCIAL"
                elif i[6] == 'E':
                    fim = "ESCRITORIO"
                else:
                    fim = "INDEFINIDO"

                jsonRetorno.setdefault((inicio), []).append({
                    'Código da Imobiliaria': i[11],
                    'Codigo do Imovel': i[0],
                    'Nome do Imovel': i[1],
                    'Endereço': i[2],
                    'Descrição': i[3],
                    'Status': status,
                    'Tipo': tipo,
                    'Finalidade': fim,
                    'Número de Quartos': i[7],
                    'Número de Salas': i[8],
                    'Número de Banheiros': i[9],
                    'Número de Vagas': i[10]
                })
                inicio = inicio + 1

            return jsonRetorno
        except Exception as err:
            print(err)
            return "Erro ao recuperar dados!"



