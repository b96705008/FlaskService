from __future__ import print_function
from __future__ import unicode_literals

from bson import ObjectId

from utils.model import MongoDBModel
from utils.query import PageQuery


class EventModel(MongoDBModel):
    fields = ['actor', 'action', 'object', 'channel']

    def query_by_page(self, cond, pagesize, page):
        query = self.collection \
            .find(cond) \
            .sort('action.time', -1)

        page_query = PageQuery(pagesize, page, query)
        return page_query.get_output()
