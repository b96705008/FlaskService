from __future__ import print_function
from __future__ import unicode_literals

import sys
import configparser
from flask import Flask
from flask import jsonify, make_response

from conf import configure_app
from api import *


# config
conf_path = sys.argv[1]
config = configparser.ConfigParser()
config.read(conf_path)

# flask app 
app = Flask(__name__)
tools = configure_app(app, config)
cache = tools['cache']
mongo = tools['mongo']

# journey query controller
journey_api = get_journey_api(config, cache, mongo)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    HOST = config.get('client', 'host')
    PORT = config.getint('client', 'port')
    URL_PREFIX = '/' + config.get('api', 'url_prefix')
    app.register_blueprint(journey_api, url_prefix=URL_PREFIX)
    app.run(debug=True, host=HOST, port=PORT)