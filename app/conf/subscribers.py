from __future__ import print_function
from __future__ import unicode_literals

from utils.basic import get_class_objs
import inspect

def register_subscribers(config, tools, models):
    from utils.basic import Subscriber
    consumer = tools['pubsub']['consumer']
    producer = tools['pubsub']['producer']
    mod = __import__('subscriber')

    Subscribers = get_class_objs(mod, Subscriber)

    for Subscriber in Subscribers:
        subscriber = Subscriber(models, producer)
        consumer.register(subscriber)
