from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint, request, jsonify

import json
from kafka import KafkaConsumer, KafkaProducer
from utils.mongodb import parse_query_to_mongo_cond


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

    ## TODO: GET /actors/<actor_id>/events


    return {'prefix': '/'+API_NAME, 'ctrler': ctrler}
