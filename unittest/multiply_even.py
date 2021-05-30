# accepts a list of numbers and returns the product of all even numbers in the list.

def multiply(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total

#print(multiply([2,3,4,5,6]))