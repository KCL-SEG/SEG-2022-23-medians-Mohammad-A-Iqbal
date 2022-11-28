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

if test == 1:
    print(str((int_numbers[int((length - 1)/2)])))

else:
    median1 = int_numbers[int((length - 1)/2)]
    median2 = int_numbers[int(((length - 1)/2) + 1)]
    print(str((median1 + median2)/2))





