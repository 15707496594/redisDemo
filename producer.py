from config import ConnectionPool, StrictRedis

url = 'redis://:admin@localhost:6379/0/'
pool = ConnectionPool.from_url(url, decode_responses=True)
# pool = ConnectionPool(host='127.0.0.1', port=6379, db=0, password='admin', decode_responses=True)
client = StrictRedis(connection_pool=pool)

for message in ['haha', 'hengheng', 'ohohohohoh']:
    client.publish('send_email', message)
