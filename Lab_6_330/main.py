from LinkedList import LinkedStack as ls
from QueueLinked import CircularQueue as cq
from Positional import PositionalList as pl
from time import time

linked = ls()
test_link = ls()
test = [3,5,2,1,6,3,5,4,3,4]

circ = cq()
test_2 = [2,3,5,1,2,3,4]
circ_2 = cq()

doub = pl()
test_3 = [4,3,2,8,9,5,7]

doub_even = pl()
test_4 = [2,3,5,7,2,0]

for i in test:
    linked.push(i)

for i in test_2:
    circ.enqueue(i)

for i in test_3:
    doub.add_first(i)

for i in test_4:
    doub_even.add_first(i)

#1
def node_count(link,og = None,n = 0):
    if link._head == None or link.__len__() == 0:
        link._head = og
        return n
    else:
        link._head = link._head._next
        return node_count(link,og, n + 1)

fill_link = (node_count(linked, linked._head))
empty_link = (node_count(test_link))

print(f"The linked list has {fill_link} nodes")
print(f"The empty list has {empty_link} nodes")

#2
def count_circ(circle,tail):
    count = 0
    circle.rotate()
    if circle._size == 0:
        return count
    else:
        count = 1
        while circle._tail != tail:
            circle.rotate()
            count += 1
        return count

filled_circ = (count_circ(circ, circ._tail))
empty_circ = (count_circ(circ_2, circ_2._tail))

print(f"This circular list has {filled_circ} nodes")
print(f"This empty list has {empty_circ} nodes")

#3
def find_middle(d):
    middle = None
    first = d._header
    start = time()
    if d.__len__() == 0:
        return middle
    else:
        if d.__len__() % 2 == 0:
            n = d.__len__() / 2
        else:
            n = int(d.__len__() / 2) + 1

        for i in range(int(n)):
            first = first._next

        end = time()
        elapsed = end - start
        return [first._element, elapsed]

odd = find_middle(doub)
even = find_middle(doub_even)

print(f"I found the middle of the odd list {odd[0]}")
print(f"The time for this first one is: {odd[1]}")
print(f"I found the middle of the even list {even[0]}")
print(f"The time for this second one is: {even[1]}")

print("The Time complexity for this program is 0(n)")



























