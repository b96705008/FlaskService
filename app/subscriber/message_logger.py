from __future__ import print_function
from __future__ import unicode_literals

import datetime as dt

from utils.basic import Subscriber


class MessageLogger(Subscriber):
    name = 'message_logger'

    def call(self, message):
        print(dt.datetime.now(), message.topic, message.value)
