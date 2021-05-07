from mypython.negocio.Imobiliaria import Imobiliaria
from mypython.persistencia.ImovelDAO import ImovelDAO


class Imovel(Imobiliaria):
    # Construtor Cheio
    def __init__(self, imobiliaria: Imobiliaria, id, nome, endereco, descricao, status, tipo, finalidade,
                 numQuartos, numSalas, numBanheiros, numVagas):
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
            ImovelDAO().insert(self)
            return "Imovel cadastrada com sucesso!"
        except:
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
            dados = ImovelDAO().selectAll()

            return dados
        except:
            return "Erro ao recuperar dados!"

    # Consulta Inteligente de acordo com o Nome
    def recuperarNomeFiltro(self, nome: str):
        try:
            dados = ImovelDAO().selectNome(nome)

            return dados
        except:
            return "Erro ao recuperar dados!"

