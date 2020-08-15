from redis import ConnectionPool

url = 'redis://:admin@localhost:6379/0/'
pool = ConnectionPool.from_url(url, decode_responses=True)