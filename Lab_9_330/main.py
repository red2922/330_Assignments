from UnsortedPrioQue import UnsortedPriorityQueue as UPQ
from SortedPrioQue import SortedPriorityQueue as SPQ
from random import randint
from time import time

PQ1 = UPQ()
PQ2 = SPQ()

sorted_list = []
unsorted_list = []

for i in range(10000):
    PQ1.add(i, randint(0, 1000))

for i in range(10000):
    PQ2.add(i, randint(0, 1000))

start_un = time()
for i in range(10000, 11000):
    PQ1.add(i, randint(0,100))
end_un = time()

start_so = time()
for i in range(10000, 11000):
    PQ2.add(i, randint(0,100))
end_so=time()

print(f"The time to add 100 to an Unsorted Queue is {end_un-start_un}")
print(f"The time to add 100 to an Sorted Queue is {end_so-start_so}")

start_del = time()
for i in range(100):
    unsorted_list.append(PQ1.remove_min())
print(unsorted_list)
end_del = time()

start_sort = time()
for i in range(100):
    sorted_list.append(PQ2.remove_min())
print(sorted_list)
end_sort = time()

print(f"The time to remove 100 from an Unsorted Queue is {end_del-start_del}")
print(f"The time to remove 100 from an Sorted Queue is {end_sort-start_sort}")