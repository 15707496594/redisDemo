from redis import StrictRedis
from config import pool
client = StrictRedis(connection_pool=pool)

# 清空db
client.flushdb()
# 判断某个key是否存在
client.exists('name')
# 设置一个key并且设置30秒的过期时间
client.setex('age', 30, 25)
client.setnx('name', 'zyh')
print(client.get('name'))
print(client.get('name'))

# 开启事务
try:
    pipe = client.pipeline()
    pipe.multi()
    pipe.hset('user:1', 'name', 'zyh')
    pipe.hset('user:1', 'age', 25)
    pipe.set('total', 100)
    pipe.execute()
    print(client.hgetall('user:1'))
except Exception as e:
    print("事务执行失败")
finally:
    client.flushdb()
    client.close()

