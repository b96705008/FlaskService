from __future__ import print_function
from __future__ import unicode_literals

import inspect


def get_class_objs(mod, super_class):
    objs = map(lambda attr: getattr(mod, attr), dir(mod))
    class_objs = filter(lambda obj: inspect.isclass(obj) and issubclass(obj, super_class), objs)
    return class_objs
