from AbstractBinaryTree import BinaryTree


class Array_Based(BinaryTree):
    def __init__(self, size):
        self._container = [None] * size
        self._size = size
        self._currsize = 0

    def __len__(self):
        return self._currsize

    #Tree Methods
    def getPosition(self, e):
        return self._container.index(e)

    def getElement(self, p):
        return self._container[p]

    def root(self):
        if self._container[0] is None:
            return None
        else:
            return 0

    #Question Num 1
    def num_children(self, p):
        count = 0

        if self.right(p) is not None:
            count += 1
        if self.left(p) is not None:
            count += 1

        return count

    #Binary Tree Methods
    def left(self, p):
        return self._container[(p * 2) + 1]

    def right(self, p):
        return self._container[(p * 2) + 2]

    def insert_root(self, e):
        if self.root() is None:
            self._container[0] = e
            self._currsize += 1
        elif self.root() is not None:
            raise ValueError("Root is already present")

    def insert_left(self, p, e):
        if self.root() is None:
            raise ValueError("No root exists")
        if self.left(p) is None and self._currsize == self._size:
            self.expand()
        if self.left(p) is None:
            self._container[(p * 2) + 1] = e
            self._currsize += 1
        else:
            raise ValueError("Left is already present")

    def insert_right(self,p, e):
        if self.root() is None:
            raise ValueError("No root exists")
        if self.right(p) is None and self._currsize == self._size:
            self.expand()
        if self.right(p) is None:
            self._container[(p * 2) + 2] = e
            self._currsize += 1
        else:
            raise ValueError("Right is already present")

    def expand(self):
        copy = self._container
        new = [None] * (self._size * 2)
        for i in range(self._size):
            new[i] = copy[i]
        self._container = new
        self._size = self._size * 2

    def printTree(self):
        for i in self._container:
            if i is None:
                pass
            else:
                print(i)

    def parent(self, p):
        if p % 2 == 0:
            return (p - 2) // 2
        else:
            return (p - 1) // 2

    def children(self, p):
        return ((p * 2) + 1, (p * 2) + 2)



