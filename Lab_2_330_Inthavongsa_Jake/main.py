import Flower
import Calculator

#1
rose = Flower.Flower("Rose", 5, 4.00)
print(rose.get_name())
print(rose.get_petals())
print(rose.get_price())


rose.set_name("White Rose")
print(rose.get_name())

#2
running = True

running_calc = Calculator.Calculator(float(input("Enter one number: ")),float(input("Enter another Number: ")),str(input("Enter a Operator(+,-,*,/): ")))
running_calc.set_accumulator()
print("The total is: " + str(running_calc.get_accumulator()))

while running:
    answer = input("Enter = to end and get total. Enter clear to reset Calculator. Otherwise enter another number: ")

    if answer == '=':
        running = False

    elif answer.lower() == 'clear':
        running_calc.clear_accumulator()

    else:
        running_calc.set_num_1(running_calc.get_accumulator())
        running_calc.set_num_2(float(answer))
        running_calc.set_operator(str(input("Enter the operator: ")))
        running_calc.set_accumulator()

        print("The total is: " + str(running_calc.get_accumulator()))


print("The total is: " + str(running_calc.get_accumulator()))

#3
lst = ["run run run away today always today away Hi Hello how are you today"]

def wordCounts(lst):
    num = lst[0].count(" ")
    lst = lst[0].split(' ', num)

    saved = {}
    for i in range(len(lst)):
        count = lst.count(lst[i])

        if lst[i] in saved:
            pass
        else:
            saved[lst[i]] = count

    return saved


def printDict(list):
    for key, value in wordCounts(list).items():
        print(str(key) + " has " + str(value) + " count.")


printDict(lst)

input_list = [input("Enter a series of words divided by spaces and I'll return counts: ")]

printDict(input_list)












