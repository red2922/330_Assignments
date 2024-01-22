import stack
#1
print("Question 1: ")
def stL(string):
    lst = []
    new_list = list(string.split(","))
    for i in new_list:
        lst.append((i))
    return lst

def lstToStack(lst, stack):
    for i in lst:
        stack.push(i)

def reverse_list(lst,stack):
    for i in lst:
        stack.push(i)

    lst.clear()
    for i in range(stack.__len__()):
        lst.append(stack.pop())

    return lst

#Hard Coded Test
test_data = [7,6,4,1,2,3,4]

stack_one = stack.Stack()
stack_two = stack.Stack()
stack_three = stack.Stack()

lstToStack(test_data, stack_one)

stack_one.transfer(stack_two)
print(stack_two.get_elements())

#Getting input
user = stL(input("Enter elements divided up by commas: "))
lstToStack(user, stack_one)
stack_one.transfer(stack_three)
print(stack_three.get_elements())

#2
print("Question 2: ")
print(stack_two.clear())
print(stack_three.clear())

#3
print("Question 3: ")
lst = ['test','run','hide','survive']
print(reverse_list(lst,stack_one))

userTwo = stL(input("Enter Elements divided up by Commas: "))
print(reverse_list(userTwo,stack_three))





