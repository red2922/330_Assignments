from queue import Empty
from Lab_9_330.PriorityQueueBase import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):

    def __iter__(self):
        current = 0
        while current != self.__len__():
            yield (self._data[current]._key, self._data[current]._value)
            current += 1

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    small_child = right
            if self._data[small_child] > self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def max(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        item = self._data[0]
        return (item._key, item._value)

    def remove_max(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

    """
    Note commented out code is used for me to keep track of what worked and what didn't
    def max(self):
        if self.is_empty():
            return Empty("Queue is empty")
        max_item = [self.__len__() - 1]
        if max_item._key

        return (max_item._key, max_item._value)

    def remove_max(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        item = self._data.pop(-1)

        return item._key, item._value
    """

    #New Functions
    def heapifyList(self, list):
        for i in list:
            self.add(i, i)

    def combineHeaps(self, o_heap):
        for i in range(o_heap.__len__()):
            self.add(o_heap._data[i]._key,o_heap._data[i]._value)

    def maxSort(self):
        local_list = []
        for i in range(self.__len__()):
            local_list.append(self.remove_max())
        return local_list

    """def maxSort(self):
        local_list = []
        for i in range(self.__len__()):
            local_list.append(self.remove_max())
        return local_list"""








