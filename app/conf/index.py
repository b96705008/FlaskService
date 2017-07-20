#from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth

from auth import configure_auth
from cache import configure_cache
from mongo import configure_mongo
from apis import load_apis
from models import load_models

# configure query app
def configure_app(app, config):
    CORS(app) # cross domain

    tools = {
        'auth': configure_auth(app, config),
        'cache': configure_cache(app, config),
        'mongo': configure_mongo(config)
    }

    models = load_models(tools['mongo'])
    apis = load_apis(config, tools, models)

    return tools, apis
