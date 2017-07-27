def init_events(models):
    event_model = models['events']
    event_model.collection.remove()

    init_events = []
    actors = ['Jenny', 'Mike']
    actions = ['eat', 'buy', 'read', 'love', 'play']
    objs = ['pizza', 'apple', 'book', 'person', 'game']

    for actor in actors:
        for time, pair in enumerate(zip(actions, objs)):
            action = pair[0]
            obj = pair[1]
            event = {
                'actor': {
                    'id': actor,
                    'type': 'customer_id'
                },
                'action': {
                    'time': time,
                    'type': action
                },
                'object': {
                    'id': obj,
                    'type': 'food'
                }
            }
            init_events.append(event)

    event_model.collection.insert_many(init_events)
    print('finish init events')

def init_tasks(models):
    task_model = models['tasks']

    # clean the storage
    task_model.collection.remove()

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
    task_model.collection.insert_many(init_tasks)
    print('finish init tasks')
