from __future__ import print_function
from __future__ import unicode_literals

from utils.mongodb import MongoDBModel
from utils.basic import get_class_objs

def load_models(config, tools):
    models = {}
    mongo = tools['mongo']
    mod = __import__('model')

    Models = get_class_objs(mod, MongoDBModel)

    for Model in Models:
        name = Model.coll_name
        collection = mongo.db[name]
        models[name] = Model(collection)

    return models
