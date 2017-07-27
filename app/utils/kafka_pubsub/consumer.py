from __future__ import print_function
from __future__ import unicode_literals

from threading import Thread
from concurrent import futures
from kafka import KafkaConsumer


class Consumer(Thread):
    daemon = True

    def __init__(self, config, subscribers=[]):
        Thread.__init__(self)
        self.group_id = config.get('kafka', 'group_id')
        self.kafka_host = config.get('kafka', 'bootstrap_servers')
        self.sub_topics = config.get('kafka', 'sub_topics').split(',')
        self.subscribers = subscribers
        self.executor = futures.ThreadPoolExecutor(max_workers=1)

    def register(self, subscriber):
        self.subscribers.append(subscriber)

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=self.kafka_host,
                                 group_id=self.group_id,
                                 auto_offset_reset='latest')
        consumer.subscribe(self.sub_topics)

        for message in consumer:
            for s in self.subscribers:
                if s.should_call(message):
                    self.executor.submit(s.call, message)
