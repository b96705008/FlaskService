from __future__ import print_function
from __future__ import unicode_literals

from utils.basic import Paginator


class MongoPaginator(Paginator):

    def __init__(self, pagesize=10, page=1, query=None):
        super(MongoPaginator, self).__init__(pagesize, page)
        self.query = query

    def set_query(self, query):
        self.query = query
        return self

    @staticmethod
    def __transform_doc(doc):
        doc['_id'] = str(doc['_id'])
        return doc

    def query_data(self):
        if self.query is None:
            raise Exception("query should be set.")

        page_query = self.query \
            .skip(self.skip) \
            .limit(self.limit)

        results = map(self.__transform_doc, page_query)

        return results
