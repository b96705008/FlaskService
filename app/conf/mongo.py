from pymongo import MongoClient


# connect MongoDB
def configure_mongo(config):
    client = MongoClient(config.get('mongo', 'uri'))
    client.db = client[config.get('mongo', 'db')]
    return client
