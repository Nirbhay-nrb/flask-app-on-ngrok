from flask_restful import Resource
import random

class TestScript(Resource):
    def get(self):
        x = random.randint(1,10)
        return {'Some random number' : x} , 200