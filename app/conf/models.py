from __future__ import print_function
from __future__ import unicode_literals

from model import *

MODEL_TYPES = ['tasks', 'events']

def load_models(mongo):
    models = {}
    for name in MODEL_TYPES:
        try:
            collection = mongo.db[name]
            if name == 'tasks':
                models[name] = TaskModel(collection)
            elif name == 'events':
                models[name] = EventModel(collection)

        except Exception as err:
            print(err)

    return models
