from __future__ import print_function
from __future__ import unicode_literals


class Model(object):

    def find(self):
        raise NotImplementedError

    def find_by_id(self, id):
        raise NotImplementedError

    def create(self, obj):
        raise NotImplementedError

    def update_by_id(self, id, obj):
        raise NotImplementedError

    def remove_by_id(self, id):
        raise NotImplementedError
