from __future__ import print_function
from __future__ import unicode_literals

from model import *


def load_models(tools):
    models = {}
    mongo = tools['mongo']
    mod = __import__('model')
    model_classes = filter(lambda m: m[-5:] == 'Model', dir(mod))

    for mc in model_classes:
        Model = getattr(mod, mc)
        name = Model.coll_name
        collection = mongo.db[name]
        models[name] = Model(collection)

    return models
