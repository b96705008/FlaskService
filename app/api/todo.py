from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint, request, jsonify, abort, make_response, url_for, current_app


def get_api(config, tools, models):
    # config
    API_NAME = config.get('api_todo', 'name')
    mongo = tools['mongo']
    task_model = models['tasks']

    # controller
    ctrler = Blueprint(API_NAME, __name__)

    @ctrler.route('/tasks', methods=['GET'])
    def list_tasks():
        # TODO


    @ctrler.route('/tasks/<task_id>', methods=['GET'])
    def get_task(task_id):
        # TODO


    @ctrler.route('/tasks', methods=['POST'])
    def create_task():
        # TODO


    @ctrler.route('/tasks/<task_id>', methods=['PUT'])
    def update_task(task_id):
        # TODO


    @ctrler.route('/tasks/<task_id>', methods=['DELETE'])
    def delete_task(task_id):
        # TODO


    return {'prefix': '/'+API_NAME, 'ctrler': ctrler}
