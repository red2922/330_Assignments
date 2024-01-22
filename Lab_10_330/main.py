from HeapPriorityQueue import HeapPriorityQueue as hpq

#Question 1
def get_three_Largest(list, heap):
    local_list = []
    for i in list:
        heap.add(i, i)
    for i in range(3):
        local_list.append(heap.remove_max())
    return local_list

excer_1 = hpq()
test = [4,3,2,1,6,7,8,10,20,40,70,60,55,100,15,25]
largest = get_three_Largest(test, excer_1)
print(largest)

#Question 2
input_count = input("Please enter the amount numbers you would like to sort: ")
print(f"You entered that you would like to sort {input_count} numbers.")

input_list = []
mix_list = [2,65,746,20,86,203,202,346,984,234]

h1 = hpq()
h2 = hpq()

for num in range(int(input_count)):
    input_num = input("Please enter number: ")
    input_list.append(int(input_num))

print(f"\nYou list is {input_list}")
print(f"This program will combine the above list with: {mix_list}")

h1.heapifyList(input_list)
h2.heapifyList(mix_list)

h1.combineHeaps(h2)
print(f'The length of the new heap is now {h1.__len__()}')


max_list = h1.maxSort()
print(f"The sorted list is:\n {max_list}")


