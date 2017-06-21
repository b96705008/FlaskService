from __future__ import print_function
from __future__ import unicode_literals

from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
from flask_cache import Cache


# cache - redis or simple(memory)
def configure_cache(app, config):
    cache_config = {
        'CACHE_TYPE': config.get('cache', 'type')
    }

    if cache_config['CACHE_TYPE'] == 'redis':
        cache_config['CACHE_REDIS_HOST'] = config.get('redis', 'host')
        cache_config['CACHE_REDIS_PORT'] = config.getint('redis', 'port')

    cache = Cache(app, config=cache_config)
    return cache


# connect MongoDB
def configure_mongo(app, config):
    app.config['MONGO_DBNAME'] = config.get('mongo', 'db')
    app.config['MONGO_URI'] = config.get('mongo', 'uri')
    mongo = PyMongo(app)
    return mongo


# configure query app
def configure_app(app, config):
    CORS(app) # cross domain
    cache = configure_cache(app, config)
    mongo = configure_mongo(app, config)

    return {'cache': cache, 'mongo': mongo}

