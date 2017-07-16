from __future__ import print_function
from __future__ import unicode_literals

# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# http://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/

class Task(object):
    fields = ['title', 'description', 'done']

    def __init__(self):
        self.tasks = []
        self.__load()

    def __load(self):
        self.tasks = [
            {
                'id': 1,
                'title': u'Buy groceries',
                'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
                'done': False
            },
            {
                'id': 2,
                'title': u'Learn Python',
                'description': u'Need to find a good Python tutorial on the web',
                'done': False
            }
        ]

    def find(self):
        return self.tasks

    def find_by_id(self, task_id):
        candid_tasks = [task for task in self.tasks if task['id'] == task_id]
        if len(candid_tasks) > 0:
            return candid_tasks[0]
        else:
            return None

    def create(self, task_obj):
        task_obj['id'] = self.tasks[-1]['id'] + 1
        self.tasks.append(task_obj)
        return task_obj

    def update_by_id(self, task_id, task_obj):
        task = self.find_by_id(task_id)
        if task is None:
            return None

        for field in self.fields:
            if field in task_obj:
                task[field] = task_obj[field]

        return task

    def remove_by_id(self, task_id):
        task = self.find_by_id(task_id)
        if task is None:
            return False
        else:
            self.tasks.remove(task)
            return True
