from __future__ import print_function
from __future__ import unicode_literals

from kafka import KafkaProducer
import json


class Producer(object):

    def __init__(self, config):
        kafka_host = config.get('kafka', 'bootstrap_servers')

        # producer
        self.pub_topic = config.get('kafka', 'pub_topic')
        self.producer = KafkaProducer(bootstrap_servers = kafka_host)

    def publish(self, pub_obj):
        self.producer.send(self.pub_topic, json.dumps(pub_obj))
