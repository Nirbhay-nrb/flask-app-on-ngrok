from flask_restful import Resource

class ServerCheck(Resource):
    def get(self):
        return {'message' : 'Server is working'} , 200