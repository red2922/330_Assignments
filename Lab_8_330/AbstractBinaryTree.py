from Abstract_Tree import Tree

class BinaryTree(Tree):
    def left(self, p):
        #Return a positions p left child
        #Return None if p does not have a left child
        raise NotImplemented('Must be implemented with as subclass')

    def right(self, p):
        #Return right child
        #Return None if p does not have right child
        raise NotImplemented('Must be implemented with as subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)