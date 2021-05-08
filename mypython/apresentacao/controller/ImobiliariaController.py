from flask_restful import Resource
from flask import jsonify
from flask import request
from mypython.negocio.Imobiliaria import Imobiliaria


cadastrarOk = {
    'status': 'Ok',
    'mensagem': 'Imobiliaria cadastrada com sucesso'
}

erroResp = {'status': 'Erro',
            'Mensagem':'Ocorreu um erro! Tente Novamente mais tarde!'}

notFound = {
    'status': 'Not Found',
    'Mensagem':'Os dados não foram encontrados'
}

erroOffsetLimit = {
    'status': 'Erro',
    'Mensagem':'Ocorreu um erro! Não foi possível fazer a consultas'
}

class ImobiliariaPostGet(Resource):
    #POST: Cadastra uma nova imobiliaria
    def post(self):
        try:
            param = request.get_json()

            if param:
                if 'id' in param:
                    if type(param['id']) is int:
                        if 'nome' in param:
                            if 'endereco' in param:
                                return jsonify({'Mensagem': Imobiliaria(param['id'], param['nome'], param['endereco']).cadastrar()})
                            else:
                                return jsonify({'status': 'Erro', 'Mensagem': 'O endereço não foi informador!'})
                        else:
                            return jsonify({'status': 'Erro', 'Mensagem': 'O nome não foi informador!'})
                    else:
                        return jsonify({'status': 'Erro', 'Mensagem': 'O id não é um numero!'})
                else:
                    return jsonify({'status': 'Erro', 'Mensagem': 'O id não informador!'})
            else:
                return jsonify({'status': 'Erro', 'Mensagem':'Nenhum dado foi informado!'})
        except Exception as err:
            return jsonify("Erro ao cadastrar nova imobiliaria")


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
                    return jsonify(Imobiliaria().recuperarTodosPage(int(ini), int(fim)))
                else:
                    return jsonify(erroOffsetLimit)


            else:
                # Recupera todos os dados
                return jsonify(Imobiliaria().recuperarTodos())

        except Exception as err:
            return jsonify(erroResp)



class ImobiliariaControllerNome(Resource):
    def get(self):
        try:
            nome = request.args.get('search')

            if nome != None:
                # Pesquisa por nome
                pesquisa = Imobiliaria().recuperarNomeFiltro(nome)

                print(pesquisa)
                if len(pesquisa) == 0:
                    return jsonify(notFound)
                else:
                    return jsonify(pesquisa)
        except Exception as err:
            return jsonify(notFound)

