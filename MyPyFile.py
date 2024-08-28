def sort_numbers(numbers):
    return sorted(numbers)

# write a function that reverses a list of numbers
def reverse_numbers(numbers):
    return list(reversed(numbers))  

# write a function that multiplies all numbers in a list by a given number
def multiply_numbers(numbers, multiplier):
    return [number * multiplier for number in numbers]

# write a test function to test the reverse_numbers function
def test_reverse_numbers():
    assert reverse_numbers([1, 2, 3]) == [3, 2, 1]
    assert reverse_numbers([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_numbers([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_numbers([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]
    assert reverse_numbers([1, 2, 3, 4, 5, 6, 7]) == [7, 6, 5, 4, 3, 2, 1]
    print("All tests passed")   



