from flask import Flask
from flask_restful import Resource, Api
from .endpoints.ImobiliariaController import ImobiliariaController

app = Flask(__name__)
api = Api(app)

api.add_resource(ImobiliariaController, '/imobi/<string:nome>')

if __name__ == '__main__':
    app.run(debug=True)