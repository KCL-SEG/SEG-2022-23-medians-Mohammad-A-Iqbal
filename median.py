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

numbers.sort()
length = len(numbers)

test = length%2

if test == 1:
    print(str((numbers[int((length - 1)/2)])))

else:
    median1 = numbers[int((length - 1)/2)]
    median2 = numbers[int(((length - 1)/2) + 1)]
    print(str((median1 + median2)/2))





