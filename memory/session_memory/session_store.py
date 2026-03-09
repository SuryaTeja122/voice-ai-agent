import redis
import json

r = redis.Redis(host="localhost", port=6379)

def save_session(session_id, data):

    r.set(session_id, json.dumps(data))

def get_session(session_id):

    data = r.get(session_id)

    if data:
        return json.loads(data)

    return {}