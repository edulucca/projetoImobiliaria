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
            #Garante que um ID igual a outro seja gravado
            validar = ImobiliariaDAO().selectAll()
            for i in validar:
                if i[0] == self.__id:
                    return "ID de Imobiliaria já cadastrado! Tente outro, por favor."

            #Valida o campo Nome*
            if self.__nome == "":
                return "Nome não foi inserido! Tente novamente!"

            ImobiliariaDAO().insert(self)
            return "Imobiliaria cadastrada com sucesso!"

        except:
            return "Erro ao cadastrar Imobiliaria!"

    #Excluir Imobiliaria
    def excluir(self, cd):
        try:
            ImobiliariaDAO().delete(cd)
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
            #Recuperar os dados do Banco de Dados
            dados = ImobiliariaDAO().selectAll()

            #Algoritimo para add os dados recperados em um dicionario com indexação
            jsonRetorno = dict()
            contador = 1
            for i in dados:
                jsonRetorno.setdefault((contador), []).append({
                    'Código da Imobiliaria': i[0],
                    'Nome da Imobiliaria': i[1],
                    'Endereço da Imobiliaria': i[2]
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
            consulta = ImobiliariaDAO().selectAll()

            #Seleciona os dados pedidos e adiciona em nova lista
            for i in range(inicio, final + 1):
                dados.append(consulta[cursor])
                cursor = cursor + 1

            #Algoritimo para add os dados recperados em um dicionario com indexação
            for i in dados:
                jsonRetorno.setdefault((inicio), []).append({
                    'Código da Imobiliaria': i[0],
                    'Nome da Imobiliaria': i[1],
                    'Endereço da Imobiliaria': i[2]
                })
                inicio = inicio + 1

            return jsonRetorno
        except:
            return "Erro ao recuperar dados!"

    #Consulta de acordo com o Nome(Não há necessidade que o nome esteja completo)
    def recuperarNomeFiltro(self, nome: str):
        try:
            # Recuperar os dados do Banco de Dados
            dados = ImobiliariaDAO().selectNome(nome)

            # Algoritimo para add os dados recperados em um dicionario com indexação
            jsonRetorno = dict()
            contador = 1
            for i in dados:
                jsonRetorno.setdefault((contador), []).append({
                    'Código da Imobiliaria': i[0],
                    'Nome da Imobiliaria': i[1],
                    'Endereço da Imobiliaria': i[2]
                })
                contador = contador + 1
            return jsonRetorno
        except:
            return "Erro ao recuperar dados!"


