from flask_cache import Cache

# cache - redis or simple(memory)
def configure_cache(app, config):
    cache_config = {
        'CACHE_TYPE': config.get('cache', 'type')
    }

    if cache_config['CACHE_TYPE'] == 'redis':
        cache_config['CACHE_REDIS_HOST'] = config.get('redis', 'host')
        cache_config['CACHE_REDIS_PORT'] = config.getint('redis', 'port')

    cache = Cache(app, config=cache_config)
    return cache
