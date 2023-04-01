def sum_of_squares(numbers):
    """
    Takes in a list of numbers and returns the sum of the sq36,uares of all the numbers in the list.
    """
    sum = 0
    for number in numbers:
        sum += number**2
    return sum
