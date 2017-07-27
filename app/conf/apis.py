from api import *


def load_apis(config, tools, models):
    apis = []
    mod = __import__('api')
    api_attrs = filter(lambda attr: attr[:3] == 'get' and attr[-3:] == 'api',
                       dir(mod))
    get_api_funcs = map(lambda attr: getattr(mod, attr), api_attrs)

    for get_api in get_api_funcs:
        apis.append(get_api(config, tools, models))
    return apis
