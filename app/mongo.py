from __future__ import print_function

import sys
import configparser

from flask import Flask
from flask import Blueprint
from flask import jsonify
from flask import request

from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
from flask_cache import Cache

from page_query import PageQuery

# config
conf_path = sys.argv[1]
config = configparser.ConfigParser()
config.read(conf_path)
HIPPO_NAME = config.get('hippo', 'name')
EVENT_COLLECION = config.get('mongo', 'collection')
DEFAULT_PAGE_SIZE = config.get('api', 'page_size')

# flask app
app = Flask(__name__)

# cross domain
CORS(app)

# cache
cache = Cache(app, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': config.get('redis', 'host'),
    'CACHE_REDIS_PORT': config.getint('redis', 'port')
})

# connect MongoDB
app.config['MONGO_DBNAME'] = config.get('mongo', 'db')
app.config['MONGO_URI'] = config.get('mongo', 'uri')
mongo = PyMongo(app)

# api service
service = Blueprint(HIPPO_NAME, __name__)

def make_key():
  """Make a key that includes GET parameters."""
  return request.full_path

@service.route('/actors/<actor_id>/events', methods=['GET'])
@cache.cached(key_prefix=make_key, timeout=10)
def get_all_events(actor_id):
    event = mongo.db[EVENT_COLLECION]
    pagesize = int(request.args.get('page_size', default=DEFAULT_PAGE_SIZE))
    page = int(request.args.get('page', default=1))
    query = event \
        .find({'actor.id': actor_id}) \
        .sort('action.time', -1)
    
    page_query = PageQuery(pagesize, page, query)
    output = page_query.get_output()
    print('query db...')
    return jsonify(output)


if __name__ == '__main__':
    HOST = config.get('client', 'host')
    PORT = config.getint('client', 'port')
    URL_PREFIX = config.get('api', 'url_prefix')
    app.register_blueprint(service, url_prefix='/' + URL_PREFIX)
    app.run(debug=True, host=HOST, port=PORT)



