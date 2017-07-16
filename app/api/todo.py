from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint, request, jsonify, abort, make_response, url_for

from model import Task


def get_api(config, cache, mongo):
    # config
    API_NAME = config.get('api_todo', 'name')
    task_model = Task()

    # controller
    ctrler = Blueprint(API_NAME, __name__)

    @ctrler.route('/tasks', methods=['GET'])
    def list_tasks():
        tasks = task_model.find()
        return jsonify({'tasks': tasks})


    @ctrler.route('/tasks/<int:task_id>', methods=['GET'])
    def get_task(task_id):
        task = task_model.find_by_id(task_id)
        if task is None:
            abort(404)
        return jsonify({'task': task})


    @ctrler.route('/tasks', methods=['POST'])
    def create_task():
        content = request.get_json()
        task = task_model.create(content)
        return jsonify({'task': task}), 201


    @ctrler.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        if not request.json:
            abort(400)

        content = request.get_json()
        task = task_model.update_by_id(task_id, content)
        if task is None:
            abort(404)
        else:
            return jsonify({'task': task})


    @ctrler.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        is_success = task_model.remove_by_id(task_id)
        if is_success:
            return jsonify({'is_success': True})
        else:
            abort(404)


    return {'prefix': '/'+API_NAME, 'ctrler': ctrler}
    
