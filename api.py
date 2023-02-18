from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world',
                'name': 'Test'}


api.add_resource(HelloWorld, '/api')


if __name__ == '__main__':
    app.run(debug=True)
