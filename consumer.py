from config import ConnectionPool, StrictRedis

url = 'redis://:admin@localhost:6379/0/'
pool = ConnectionPool.from_url(url, decode_responses=True)
client = StrictRedis(connection_pool=pool)

consumer = client.pubsub()
consumer.subscribe('send_email')
for item in consumer.listen():
    print(item)
