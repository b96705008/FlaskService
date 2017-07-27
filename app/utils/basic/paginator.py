from __future__ import print_function
from __future__ import unicode_literals


class Paginator(object):

    def __init__(self, pagesize=10, page=1):
        self.params = {
            'pagesize': pagesize,
            'page': page
        }
        self.has_next = True

    def set(self, name, value):
        if name in self.params:
            self.params[name] = value
        return self

    @property
    def skip(self):
        return (self.params['page'] - 1) * self.params['pagesize']

    @property
    def limit(self):
        return self.params['pagesize'] + 1

    def get_next_page(self):
        next_page = {
            'has_next': self.has_next
        }

        if self.has_next:
            next_page['page'] = self.params['page'] + 1
            next_page['page_size'] = self.params['pagesize']

        return next_page

    def query_data(self):
        raise NotImplementedError

    def build_output(self, results):
        output = {
            'data_count': len(results),
            'result': results,
            'next_page': self.get_next_page()
        }
        return output

    def get_output(self):
        results = self.query_data()

        if len(results) < self.limit:
            self.has_next = False

        results = results[:self.params['pagesize']]
        output = self.build_output(results)

        return output
