import uuid
import json
import redis
import os

class Session:

    def __init__(self):
        redis_url = os.getenv('REDIS_URL')
        if not redis_url:
            raise Exception("App can't be started without a REDIS_URL")
        self.db = redis.Redis.from_url(redis_url)

    def create_session(self):
        session_id = str(uuid.uuid4())
        self.db.set(f"session_{session_id}", json.dumps([]), 600)
        return session_id
    
    def get_session(self, session_id):
        return json.loads(self.db.get(session_id))

    def update_history(self, session_id, content):
        session_data = self.get_session(f"session_{session_id}")
        session_data.append(content)
        self.db.set(f"session_{session_id}", json.dumps(session_data))