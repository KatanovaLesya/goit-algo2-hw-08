import time
from typing import Dict


class ThrottlingRateLimiter:
    def __init__(self, min_interval: float = 10.0):
        self.min_interval = min_interval
        self.last_message_time: Dict[str, float] = {}

    def can_send_message(self, user_id: str) -> bool:
        current_time = time.time()
        last_time = self.last_message_time.get(user_id)
        if last_time is None:
            return True
        return (current_time - last_time) >= self.min_interval

    def record_message(self, user_id: str) -> bool:
        if self.can_send_message(user_id):
            self.last_message_time[user_id] = time.time()
            return True
        return False

    def time_until_next_allowed(self, user_id: str) -> float:
        current_time = time.time()
        last_time = self.last_message_time.get(user_id)
        if last_time is None:
            return 0.0
        return max(0.0, self.min_interval - (current_time - last_time))
