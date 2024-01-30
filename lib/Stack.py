class Stack:
    def __init__(self, items=None, max_size=None):
        if items is None:
            items = []
        self.items = items
        self.max_size = max_size

    def push(self, item):
        if self.max_size is None or len(self.items) < self.max_size:
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def full(self):
        if self.max_size is not None and self.size() >= self.max_size:
            return True
        return False

    def search(self, target):
        for index, item in enumerate(self.items):
            if item == target:
                return self.size() - index - 1
        return -1