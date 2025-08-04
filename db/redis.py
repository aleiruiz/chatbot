import redis
import os

client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")) if os.getenv("REDIS_PORT") else 6379,
    password=os.getenv("REDIS_PASSWORD"),
    ssl=os.getenv("REDIS_SSL") == "true",
    decode_responses=True,
)


def test_redis_connection():
    """
    Test Redis connection.
    """
    try:
        client.ping()
        print("Redis connection successful.")
        return True
    except redis.ConnectionError:
        return False


def get_session(name):
    """
    Get session by username.
    """
    return client.get(name)


def set_session(name, value):
    """
    Set session by username.
    """
    client.set(name, value, ex=1800)  # Set expiration time to half an hour
    return True
