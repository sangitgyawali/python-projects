class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0


counter = Counter()
counter.increment()
counter.increment()
print("Count:", counter.count)
counter.decrement()
print("Count:", counter.count)
counter.reset()
print("Count:", counter.count)