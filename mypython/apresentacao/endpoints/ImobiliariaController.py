from flask_restful import Resource
from flask import jsonify
from ...negocio.Imobiliaria import Imobiliaria

obj_imobi = Imobiliaria("Eduardo", "Brasil")


class ImobiliariaController(Resource):
    def get(self, nome):
        return jsonify({'Nome': obj_imobi.getNome(), 'Endereco': obj_imobi.getEndereco()})
