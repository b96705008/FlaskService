from __future__ import print_function
from __future__ import unicode_literals

from bson import ObjectId

from utils.model import MongoDBModel


class TaskModel(MongoDBModel):
    fields = ['title', 'description', 'done']

    def on_init(self):
        print('Refresh task data...')
        # clean the storage
        self.collection.remove()

        # insert initial data
        init_tasks = [
            {
                'title': u'Buy groceries',
                'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
                'done': False
            },
            {
                'title': u'Learn Python',
                'description': u'Need to find a good Python tutorial on the web',
                'done': False
            }
        ]
        self.collection.insert_many(init_tasks)
        return self
