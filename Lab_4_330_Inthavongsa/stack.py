class Stack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise "Stack is Empty"
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise "Stack is Empty"
        return self._data.pop()

    def transfer(self, T):
        for i in range(self.__len__()):
            T.push(self.pop())

    def get_elements(self):
        return self._data

    def clear(self):
        if self.is_empty() == False:
            self.pop()
            self.clear()
        else:
            self.get_elements()

