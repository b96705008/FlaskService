from __future__ import print_function
from __future__ import unicode_literals


class PageQuery(object):
    
    def __init__(self, pagesize, page, basic_query):
        self.pagesize = pagesize
        self.page = page
        self.has_next = True
        self.page_query = basic_query \
            .skip(self.skip) \
            .limit(self.limit)

    @property
    def skip(self):
        return (self.page - 1) * self.pagesize

    @property
    def limit(self):
        return self.pagesize + 1

    @staticmethod
    def map_doc(d): 
        d['_id'] = str(d['_id'])
        return d

    def __get_next_page(self):
        next_page = {
            'has_next': self.has_next
        }

        if self.has_next:
            next_page['page'] = self.page + 1
            next_page['page_size'] = self.pagesize
            next_page['next_page_url'] = '?page_size={}&page={}' \
                .format(next_page['page_size'], next_page['page'])

        return next_page

    def get_output(self):
        results = map(self.map_doc, self.page_query)

        if len(results) < self.limit:
            self.has_next = False

        results = results[:self.pagesize]
        next_page = self.__get_next_page()

        return {'result': results, 'next_page': next_page}