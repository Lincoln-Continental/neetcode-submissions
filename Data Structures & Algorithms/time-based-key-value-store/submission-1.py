class TimeMap:
    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = {}
        if timestamp not in self.storage[key]:
            self.storage[key][timestamp] = []
        self.storage[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        
        seen = 0
        for time in self.storage[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.storage[key][seen][-1]
