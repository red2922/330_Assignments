from Queue import ArrayQueue as aq
from Array_stack import Stack as st
from DeQueue import ArrayDeQueue as dq

q = aq()
s = st()
d = dq()

#1

def elem_in_stack(s, q, x):
    elem = False
    while s.__len__() >= 1:
        q.enqueue(s.pop())

    while q.__len__() >= 1:
        if q.first() == x:
            elem = True
        s.push(q.dequeue())

    while s.__len__() >= 1:
        q.enqueue(s.pop())

    while q.__len__() >= 1:
        s.push(q.dequeue())

    return elem

test = [1, 2, 3, 4, 5, 6]

for i in test:
    s.push(i)

num = input("Input a number: ")
print(elem_in_stack(s,q,num))
print(elem_in_stack(s, q, 3))
print(s.get_elements())
print(q.get_e())

#2
dq_test = [1,2,3,4]

for i in dq_test:
    d.enqueue(i)

d.remove_tail()
d.insert_head(5)
d.insert_head((7))

print(d.get_e())







