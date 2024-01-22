import Part_1
import Part_2
import Part_3

#1
test = [7,6,3,8,10,12]
print(Part_1.minandMax(test,0,0,0))

ui = Part_1.stringToListInt(input("Please enter a list of numbers broken up by commas: "))
print(Part_1.minandMax(ui,0,0,0))


#2
new_list = []
print(Part_2.r_string(str(input("Enter a string: ")),new_list))


#3
new_test = [12,23,45,67,53,84,36,76,23]

print(Part_3.evenOdd(new_test))
ui_2 = Part_1.stringToListInt(input("Please enter a list of numbers broken up by commas: "))

print(Part_3.evenOdd(ui_2))
