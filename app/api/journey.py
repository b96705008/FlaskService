from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint, request, jsonify

from utils.query import build_mongo_query_cond


def get_api(config, tools, models):
    # config
    API_NAME = config.get('api_journey', 'name')
    DEFAULT_PAGE_SIZE = config.get('api_journey', 'page_size')
    CACHE_TIMEOUT_SECS = config.getint('cache', 'timeout')
    cache = tools['cache']
    mongo = tools['mongo']
    auth = tools['auth']
    event_model = models['events']

    # controller
    ctrler = Blueprint(API_NAME, __name__)

    def make_cache_key():
      """Make a key that includes GET parameters."""
      return request.full_path

    # route
    @ctrler.route('/actors/<actor_id>/events', methods=['GET'])
    @cache.cached(key_prefix=make_cache_key, timeout=CACHE_TIMEOUT_SECS)
    def get_actor_events(actor_id):
        pagesize = int(request.args.get('_page_size', default=DEFAULT_PAGE_SIZE))
        page = int(request.args.get('_page', default=1))

        # parse condition
        cond = build_mongo_query_cond(request.args, {
                'actor.id': actor_id
            })
        output = event_model.query_by_page(cond, pagesize, page)
        return jsonify(output)


    @ctrler.route('/events', methods=['GET'])
    @auth.login_required
    def list_all_events():
        return jsonify({'events': [e for e in event_model.find()]})


    return {'prefix': '/'+API_NAME, 'ctrler': ctrler}
