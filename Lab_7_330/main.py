from PositionalList import PositionalList as pL

#1
def max(L):
    maxNum = 0
    if L.is_empty():
        maxNum = None
    else:
        for i in L:
            if i > maxNum:
                maxNum = i
    return maxNum

position_list = pL()
test_list = pL()
test = [10,20,292,762,853,2,0]

for i in test:
    position_list.add_last(i)

print(f"The max value in the positional list is: {max(position_list)}")
print(f'The max value for this positional list is: {max(test_list)}')
#2
def printPos(p, i):
    position = p
    numPos = i
    if position == None:
        position = 'None'
        numPos = 'None'
        element = 'None'
    else:
        position = p
        element = p.element()

    print(f"The address position of {element} is {position}")
    print(f"The index position of {element} is {numPos}")

found, count_1 = position_list.find_e(7)
found_2, count_2  = position_list.find_e(292)

printPos(found, count_1)
printPos(found_2, count_2)

#3
for i in position_list:
    print(i)

print()

for i in reversed(position_list):
    print(i)