import redis

redis_config = {
    'host': '127.0.0.1',
    'port': 6379
}

redis_connect = redis.Redis(**redis_config)

value = redis_connect.get('key')
value2 = redis_connect.get('key2')
print(value, value2)

