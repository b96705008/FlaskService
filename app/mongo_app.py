from __future__ import print_function
from __future__ import unicode_literals

import sys
import configparser

from flask import Flask
from flask import Blueprint
from flask import jsonify
from flask import request

# from flask_pymongo import PyMongo
# from flask_cors import CORS, cross_origin
# from flask_cache import Cache
from env import configure_app
from utils import PageQuery, build_mongo_query_cond

# config
conf_path = sys.argv[1]
config = configparser.ConfigParser()
config.read(conf_path)

# flask app 
app = Flask(__name__)
tools = configure_app(app, config)
cache = tools['cache']
mongo = tools['mongo']

# sub service
HIPPO_NAME = config.get('hippo', 'name')
service = Blueprint(HIPPO_NAME, __name__)

# other config params
EVENT_COLLECION = config.get('mongo', 'collection')
DEFAULT_PAGE_SIZE = config.get('api', 'page_size')
CACHE_TIMEOUT_SECS = config.get('cache', 'timeout')


def make_cache_key():
  """Make a key that includes GET parameters."""
  return request.full_path


@service.route('/actors/<actor_id>/events', methods=['GET'])
@cache.cached(key_prefix=make_cache_key, timeout=CACHE_TIMEOUT_SECS)
def get_all_events(actor_id):
    event = mongo.db[EVENT_COLLECION]
    pagesize = int(request.args.get('_page_size', default=DEFAULT_PAGE_SIZE))
    page = int(request.args.get('_page', default=1))
    
    # parse condition
    cond = build_mongo_query_cond(request.args, {
            'actor.id': actor_id
        }) 

    # query mongodb
    query = event \
        .find(cond) \
        .sort('action.time', -1)
    
    page_query = PageQuery(pagesize, page, query)
    output = page_query.get_output()
    return jsonify(output)


if __name__ == '__main__':
    HOST = config.get('client', 'host')
    PORT = config.getint('client', 'port')
    URL_PREFIX = '/' + config.get('api', 'url_prefix')
    app.register_blueprint(service, url_prefix=URL_PREFIX)
    app.run(debug=True, host=HOST, port=PORT)



