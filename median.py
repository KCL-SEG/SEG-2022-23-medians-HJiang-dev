"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
if len(numbers)%2 == 1:
    median = numbers[len(numbers)//2 ]
else:
    median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2 ])/2






print (numbers)
print (median)
