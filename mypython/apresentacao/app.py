from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from mypython.apresentacao.controller.ImobiliariaController import ImobiliariaPostGet, ImobiliariaControllerNome
from mypython.apresentacao.controller.ImovelController import ImovelPostGet, ImovelControllerNome
from mypython.negocio.Imobiliaria import Imobiliaria
from mypython.negocio.Imovel import Imovel

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)


#Rotas da API

#IMOBILIARIAS

#GET/POST:
#Lista todos as imobiliarias, lista imobiliarias com paginação offset/limit,
api.add_resource(ImobiliariaPostGet, '/api/imobiliarias')

#Lista todas as imobiliarias tendo como referencia o nome da imobiliria
api.add_resource(ImobiliariaControllerNome, '/api/imobiliarias/nome')

#DELETE:
#Deleta uma imobiliaria e os seus imoveis correspondentes a partir do ID de Imobiliaria
@app.route('/api/imobiliarias/<int:id>', methods=['DELETE'])
def delete_imobiliaria(id):
    try:
        Imobiliaria().excluir(id)
        return jsonify("Imobiliaria Excluida!")
    except Exception as err:
        return jsonify("Não foi possível excluir imobiliaria!")

#UPDATE:
#Altera os dados de uma imobiliaria de acordo com o id informado
@app.route('/api/imobiliarias/<int:id>', methods=['PUT'])
def update_imobiliaria(id):
    try:
        param = request.get_json()

        Imobiliaria.alterar(Imobiliaria(id, param['nome'], param['endereco']))
        return jsonify("Os dados da imobiliaria foram alterados com sucesso")
    except Exception as err:
        return jsonify("Ocorreu um erro! Tente novamente!")


#IMOVEIS

#GET/POST
#Lista todos os imoveis, lista imoveis com paginação offset/limit,
api.add_resource(ImovelPostGet, '/api/imoveis')
#Pesquisa o nome especifico de uma casa usando a chave "search"
api.add_resource(ImovelControllerNome, '/api/imoveis/nome')

#DELETE:
#Deleta um imovel a partir do ID de Imobiliaria
@app.route('/api/imoveis/<int:id>', methods=['DELETE'])
def delete_imovel(id):
    try:
        Imovel().excluir(id)
        return jsonify("Imóvel Excluida!")
    except Exception as err:
        return jsonify("Não foi possível excluir Imóvel!")

#UPDATE:
#Altera os dados de um imovel de acordo com o id informado
@app.route('/api/imoveis/<int:id>', methods=['PUT'])
def update_imovel(id):
    try:
        param = request.get_json()

        Imovel.alterar(Imovel(Imobiliaria(id=param['id_imobiliaria']), id, param['nome'],
                                               param['endereco'], param['descricao'], param['status'], param['tipo'],
                                               param['finalidade'], param['num_quartos'], param['num_salas'],param['num_banheiros'],
                                               param['num_vagas']))

        return jsonify("Os dados do imovel foram alterados com sucesso")
    except Exception as err:
        return jsonify("Ocorreu um erro! Tente novamente!")
if __name__ == '__main__':
    app.run(debug=True)