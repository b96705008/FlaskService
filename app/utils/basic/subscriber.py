from __future__ import print_function
from __future__ import unicode_literals


class Subscriber(object):
    name = None

    def __init__(self, models, producer):
        self.models = models
        self.producer = producer

    def should_call(self, message):
        return True

    def call(self, message):
        raise NotImplementedError
