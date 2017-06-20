from __future__ import print_function

import sys
import configparser

from flask import Flask
from flask import jsonify
from flask import request

from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

from page_query import PageQuery

# config
conf_path = sys.argv[1]
config = configparser.ConfigParser()
config.read(conf_path)
EVENT_COLLECION = config.get('mongo', 'collection')
DEFAULT_PAGE_SIZE = config.get('api', 'page_size')

# flask app
app = Flask(__name__)

# cross domain
CORS(app)

# connect MongoDB
app.config['MONGO_DBNAME'] = config.get('mongo', 'db')
app.config['MONGO_URI'] = config.get('mongo', 'uri')
mongo = PyMongo(app)


@app.route('/actors/<actor_id>/events', methods=['GET'])
def get_all_events(actor_id):
    event = mongo.db[EVENT_COLLECION]
    pagesize = int(request.args.get('page_size', default=DEFAULT_PAGE_SIZE))
    page = int(request.args.get('page', default=1))

    query = event \
        .find({'actor.id': actor_id}) \
        .sort('action.time', -1)
    
    page_query = PageQuery(pagesize, page, query)
    output = page_query.get_output()
    return jsonify(output)


if __name__ == '__main__':
    HOST = config.get('client', 'host')
    PORT = config.getint('client', 'port')
    app.run(debug=True, host=HOST, port=PORT)



