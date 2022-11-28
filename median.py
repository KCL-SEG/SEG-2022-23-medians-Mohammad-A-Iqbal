"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

int_numbers = [int(i) for i in numbers]    

int_numbers.sort()

length = len(int_numbers)

test = length%2

print(numbers)
median  = "The median for the list is: "

if test == 1:
    median += str((int_numbers[int((length - 1)/2)]))

else:
    median1 = int_numbers[int((length - 1)/2)]
    median2 = int_numbers[int(((length - 1)/2) + 1)]
    median += str((median1 + median2)/2)



print(median)


