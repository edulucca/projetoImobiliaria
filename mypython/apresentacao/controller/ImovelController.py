from flask import request, jsonify
from flask_restful import Resource
from mypython.negocio.Imovel import Imovel
from mypython.negocio.Imobiliaria import Imobiliaria

class ImovelPostGet(Resource):
    #POST: Cadastra uma nova imobiliaria
    def post(self):
        try:
            param = request.get_json()

            return jsonify({'Mensagem': Imovel(Imobiliaria(id=param['id_imobiliaria']), param['id_imovel'], param['nome'],
                                               param['endereco'], param['descricao'], param['status'], param['tipo'],
                                               param['finalidade'], param['num_quartos'], param['num_salas'],param['num_banheiros'],
                                               param['num_vagas']).cadastrar()})

        except Exception as err:
            return jsonify("Erro ao cadastrar imóvel!")


    #GET: Listar todas as imobiliarias
    def get(self):
        try:
            # parametro de requisição com paginação
            ini = request.args.get('offset')
            fim = request.args.get('limit')
            # Parametro de pesquisa por nome

            # Verifica se as chaves foram inseridas
            if ini != None:
                if fim != None:
                        # Paginação:offset/limit
                        return jsonify(Imovel().recuperarTodosPage(int(ini), int(fim)))
                else:
                    return jsonify("Erro ao classificar os dados de imovel!Tente Novamente!")
            else:
                # Recupera todos os dados

                return jsonify(Imovel().recuperarTodos())

        except Exception as err:
            print(err)
            return jsonify("Erro ao recuperar dados do Imóvel")

class ImovelControllerNome(Resource):
    def get(self):
        try:
            nome = request.args.get('search')
            if nome != None:
                # Pesquisa por nome
                pesquisa = Imovel().recuperarNomeFiltro(nome)
                print(pesquisa)
                if len(pesquisa) == 0:
                    return jsonify("Imovel não encontrado!")
                else:
                    return jsonify(pesquisa)
        except Exception as err:
            return jsonify("Ocorreu um erro durante a pesquisa!")
