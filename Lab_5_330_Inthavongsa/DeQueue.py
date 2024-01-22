from queue import Empty


class ArrayDeQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def get_e(self):
        return self._data

    def insert_head(self, e):
        lst = []
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        while self._size >= 1:
            lst.append(self.dequeue())

        self._front = 0
        self._size = 0

        self.enqueue(e)

        for i in lst:
            self.enqueue(i)


    def remove_tail(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        self._data[self._size - 1] = None
        self._size -= 1










