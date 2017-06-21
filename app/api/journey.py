from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint, request, jsonify

from utils import PageQuery, build_mongo_query_cond


def get_api(config, cache, mongo):
    # config
    HIPPO_NAME = config.get('hippo', 'name')
    EVENT_COLLECION = config.get('mongo', 'collection')
    DEFAULT_PAGE_SIZE = config.get('api', 'page_size')
    CACHE_TIMEOUT_SECS = config.get('cache', 'timeout')

    # controller
    api = Blueprint(HIPPO_NAME, __name__)

    def make_cache_key():
      """Make a key that includes GET parameters."""
      return request.full_path

    # route
    @api.route('/actors/<actor_id>/events', methods=['GET'])
    @cache.cached(key_prefix=make_cache_key, timeout=CACHE_TIMEOUT_SECS)
    def get_all_events(actor_id):
        event = mongo.db[EVENT_COLLECION]
        pagesize = int(request.args.get('_page_size', default=DEFAULT_PAGE_SIZE))
        page = int(request.args.get('_page', default=1))
        
        # parse condition
        cond = build_mongo_query_cond(request.args, {
                'actor.id': actor_id
            }) 

        # query mongodb
        query = event \
            .find(cond) \
            .sort('action.time', -1)
        
        page_query = PageQuery(pagesize, page, query)
        output = page_query.get_output()
        return jsonify(output)

    return api
