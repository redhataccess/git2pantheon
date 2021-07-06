import redis
import os
import logging

from redis.exceptions import RedisError


def initialize_broker():
    if 'REDIS_SERVICE' not in os.environ:
        logging.error('REDIS_SERVICE is not set in environment variables. Status API would be impacted')
    redis_conn = redis.Redis(host=os.getenv('REDIS_SERVICE'), decode_responses=True)
    try:
        redis_conn.ping()
    except RedisError as redis_error:
        logging.error('Could not connect to Redis instance. Status API would be impacted')
    return redis_conn


broker = initialize_broker()
