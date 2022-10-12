# imports
from flask import Flask
from flask_restful import Api
from flask_ngrok import run_with_ngrok

from resources.server_check import ServerCheck
from resources.testscript import TestScript

# creating the app
app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'ngrokFlaskApp'
api = Api(app)
run_with_ngrok(app)

# adding resources
api.add_resource(ServerCheck , '/checkServer')
api.add_resource(TestScript , '/testScript')


# running the app
if __name__ == '__main__':
    app.run()