from threading import Thread
from kafka import KafkaConsumer, KafkaProducer
import json


class Consumer(Thread):
    daemon = True

    def __init__(self, config):
        Thread.__init__(self)
        self.group_id = config.get('kafka', 'group_id')
        self.kafka_host = config.get('kafka', 'bootstrap_servers')
        self.sub_topics = config.get('kafka', 'sub_topics').split(',')

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=self.kafka_host,
                                 group_id=self.group_id,
                                 auto_offset_reset='latest')
        consumer.subscribe(self.sub_topics)

        for message in consumer:
            print (message)


class MessageClient(object):

    def __init__(self, config):
        kafka_host = config.get('kafka', 'bootstrap_servers')

        # producer
        self.pub_topic = config.get('kafka', 'pub_topic')
        self.producer = KafkaProducer(bootstrap_servers = kafka_host)

        # consumer
        self.consumer = Consumer(config)
        self.consumer.start()

    def send_msg(self, pub_obj):
        print('ready to sent msg...')
        self.producer.send(self.pub_topic, json.dumps(pub_obj))


# connect kafka consumer and producer
def configure_kafka(config):
    client = MessageClient(config)
    return client
