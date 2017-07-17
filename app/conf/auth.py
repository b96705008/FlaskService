from flask_httpauth import HTTPBasicAuth
from flask import jsonify, make_response


def configure_auth(app, config):
    auth = HTTPBasicAuth()

    @auth.get_password
    def get_password(username):
        # fetch pwd from db
        if username == 'root':
            return '1234'
        return None

    @auth.error_handler
    def unauthorized():
        return make_response(jsonify({'error': 'Unauthorized access'}), 401)

    return auth
