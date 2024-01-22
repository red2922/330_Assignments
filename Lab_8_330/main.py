from Array_Based_Binary import Array_Based

tree = Array_Based(20)

tree.insert_root('A')
#tree.insert_root(10)
tree.insert_left(0, 'B')
tree.insert_right(0, 'C')
tree.insert_left(1, 'D')
tree.insert_right(1, 'E')
tree.insert_left(2, 'F')
tree.printTree()

print(f"The number of children for position 0 is : {tree.num_children(0)}")
print(f"The number of children for position 1 is : {tree.num_children(1)}")
print(f"The number of children for position 2 is : {tree.num_children(2)}")
print(f"The number of children for position 3 is : {tree.num_children(3)}")

print(f"The parent of position 2 is {tree.parent(2)}")
print(f"The parent of position 4 is {tree.parent(4)}")
print(f"The children positions are {tree.children(0)}")

print(f"The root position is: {tree.root()}")
print(f"The root element is: {tree.getElement(tree.root())}")
print(f"The length of the tree is: {tree.__len__()}")

