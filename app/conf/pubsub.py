from __future__ import print_function
from __future__ import unicode_literals

from utils.kafka_pubsub import *


# connect kafka consumer and producer
def configure_kafka(config):
    consumer = Consumer(config)
    consumer.start()

    producer = Producer(config)

    return { 'consumer': consumer, 'producer': producer }
