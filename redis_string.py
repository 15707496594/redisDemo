from config import pool
from redis import StrictRedis

client = StrictRedis(connection_pool=pool)

try:
    print(client.set('name', 'zyh')) # True
    print(client.append('name', 'ZYH')) # 6
    print(client.get('name')) # zyhZYH
    print(client.keys('*')) # ['name']
    print(client.strlen('name')) # 6
    print(client.append('age', 25)) # 2
    print(client.get('age')) # 25
    print(type(client.get('age'))) # <class 'str'>
except Exception as e:
    print(e)
finally:
    if client:
        client.flushdb()
        client.close()