from __future__ import print_function
from __future__ import unicode_literals

from bson import ObjectId

from utils.mongodb import MongoDBModel


class TaskModel(MongoDBModel):
    coll_name = 'tasks'
    fields = ['title', 'description', 'done']
