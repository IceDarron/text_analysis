# encoding=utf-8
import redis

# 连接池
pool = redis.ConnectionPool(host="127.0.0.1", port=6379, password="123456", max_connections=1024)
conn = redis.Redis(connection_pool=pool)


def get_connector():
    return conn


if __name__ == '__main__':
    conn = get_connector()
    conn.set("x1", "hello", ex=10)  # ex代表seconds，px代表ms
    val = conn.get("x1")
    print(conn.get("x1"))
