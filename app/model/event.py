from __future__ import print_function
from __future__ import unicode_literals

from bson import ObjectId

from utils.mongodb import MongoDBModel
from utils.mongodb import MongoPaginator


class EventModel(MongoDBModel):
    coll_name = 'events'
    fields = ['actor', 'action', 'object', 'channel']
    

    def query_by_page(self, cond, pagesize, page):
        query = self.collection \
            .find(cond) \
            .sort('action.time', -1)

        paginator = MongoPaginator(pagesize, page, query)

        return paginator.get_output()
