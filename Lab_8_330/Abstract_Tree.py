class Tree:

    class Position:

        def element(self):
            raise NotImplemented('Must be implemented with as subclass')

        def __eq__(self, other):
            return self == other

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplemented('Must be implemented with as subclass')

    def parent(self, p):
        raise NotImplemented('Must be implemented with as subclass')

    def num_children(self, p):
        raise NotImplemented('Must be implemented with as subclass')

    def children(self, p):
        raise NotImplemented('Must be implemented with as subclass')

    def __len__(self):
        raise NotImplemented('Must be implemented with as subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0


