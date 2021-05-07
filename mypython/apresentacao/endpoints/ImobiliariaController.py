from flask_restful import Resource
from flask import jsonify
from ...negocio.Imobiliaria import Imobiliaria

obj_imobi = Imobiliaria("Eduardo", "Brasil")


class ImobiliariaController(Resource):
    #GET: Listar todas as imobiliarias
    def get(self, nome):
        return jsonify({'Nome': obj_imobi.nome(), 'Endereco': obj_imobi.endereco()})
