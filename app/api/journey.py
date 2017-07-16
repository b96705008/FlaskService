from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint, request, jsonify

from utils import PageQuery, build_mongo_query_cond


def get_api(config, cache, mongo):
    # config
    API_NAME = config.get('api_journey', 'name')
    EVENT_COLLECION = config.get('api_journey', 'collection')
    DEFAULT_PAGE_SIZE = config.get('api_journey', 'page_size')
    CACHE_TIMEOUT_SECS = config.getint('cache', 'timeout')

    # controller
    ctrler = Blueprint(API_NAME, __name__)

    def make_cache_key():
      """Make a key that includes GET parameters."""
      return request.full_path

    # route
    @ctrler.route('/actors/<actor_id>/events', methods=['GET'])
    @cache.cached(key_prefix=make_cache_key, timeout=CACHE_TIMEOUT_SECS)
    def get_all_events(actor_id):
        event_coll = mongo.db[EVENT_COLLECION]
        pagesize = int(request.args.get('_page_size', default=DEFAULT_PAGE_SIZE))
        page = int(request.args.get('_page', default=1))

        # parse condition
        cond = build_mongo_query_cond(request.args, {
                'actor.id': actor_id
            })

        # query mongodb
        query = event_coll \
            .find(cond) \
            .sort('action.time', -1)

        page_query = PageQuery(pagesize, page, query)
        output = page_query.get_output()
        return jsonify(output)

    return {'prefix': '/'+API_NAME, 'ctrler': ctrler}
