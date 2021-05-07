from mypython.persistencia.ImobiliariaDAO import ImobiliariaDAO


class Imobiliaria:

    # Construtor da classe
    def __init__(self, id=0, nome="", endereco=""):
        self.__id = id
        self.__nome = nome
        self.__endereco = endereco

    # Métodos Get/Set da Classe
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


    #Métodos de Persistencia da Classe
    #Cadastrar Imobiliaria
    def cadastrar(self):
        try:
            ImobiliariaDAO().insert(self)
            return "Imobiliaria cadastrada com sucesso!"
        except:
            return "Erro ao cadastrar Imobiliaria!"

    #Excluir Imobiliaria
    def excluir(self, id: int):
        try:
            ImobiliariaDAO().delete(id)
            return "Imobiliaria excluida com sucesso!"
        except:
            return "Erro ao excluir Imobiliaria!"

    #Alterar os dados de uma imobiliairia a partir da ID
    def alterar(self):
        try:
            ImobiliariaDAO().update(self)
            return "Imobiliaria atualizada com sucesso!"
        except:
            return "Erro ao atualizar Imobiliaria!"

    #Consulta todos os dados de Imobiliaria e salva em uma lista
    def recuperarTodos(self):
        try:
            dados = ImobiliariaDAO().selectAll()

            return dados
        except:
            return "Erro ao recuperar dados!"

    #Consulta de acordo com o Nome(Não há necessidade que o nome esteja completo)
    def recuperarNomeFiltro(self):
        try:
            dados = ImobiliariaDAO().selectNome(self)

            return dados
        except:
            return "Erro ao recuperar dados!"


