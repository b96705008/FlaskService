from __future__ import print_function
from __future__ import unicode_literals


class PageQuery(object):

    def __init__(self, pagesize=10, page=1, basic_query=None):
        self.params = {
            'pagesize': pagesize,
            'page': page,
            'basic_query': basic_query
        }
        self.has_next = True

    def set(self, name, value):
        if name in self.params:
            self.params[name] = value
        return self

    @staticmethod
    def __transform_doc(doc):
        doc['_id'] = str(doc['_id'])
        return doc

    @property
    def skip(self):
        return (self.params['page'] - 1) * self.params['pagesize']

    @property
    def limit(self):
        return self.params['pagesize'] + 1

    def __get_next_page(self):
        next_page = {
            'has_next': self.has_next
        }

        if self.has_next:
            next_page['page'] = self.params['page'] + 1
            next_page['page_size'] = self.params['pagesize']

        return next_page

    def get_output(self):
        if not self.params['basic_query']:
            raise Exception("bascic query should be given.")

        self.page_query = self.params['basic_query'] \
            .skip(self.skip) \
            .limit(self.limit)

        results = map(self.__transform_doc, self.page_query)

        if len(results) < self.limit:
            self.has_next = False

        results = results[:self.params['pagesize']]
        data_count = len(results)
        next_page = self.__get_next_page()
        output = {
            'data_count': data_count,
            'result': results,
            'next_page': next_page
        }

        return output
