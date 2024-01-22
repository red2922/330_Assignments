from AbstractBinaryTree import BinaryTree

class newTree(BinaryTree):
    class Position:
        def __init__(self, element):
            self._element = element

        def getElement(self):
            return self._element


    def __init(self):
        self._container = [None] * 10

    def root(self):
        return self._container[0]

    def insert_root(self, e):
        if self.root() is None:
            self._container[0] = Position(e)


