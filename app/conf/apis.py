from api import *


def load_apis(config, tools, models):
    apis = []
    for get_api in [get_todo_api, get_journey_api]:
        apis.append(get_api(config, tools, models))
    return apis
