def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == []:
        return None

    minimum = float('inf')
    maximum = float('-inf')
    for i in ints:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return (minimum, maximum)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

#own test_cases
print("Test Case 1 - Empty Array -> Return None")
input = []
solution = None
output = get_min_max(input)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - length == 1")
input = [1]
solution = (1, 1)
output = get_min_max(input)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - contains negative values")
input = [-1, -5, -10, -22]
solution = (-22, -1)
output = get_min_max(input)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - positive and negative values")
input = [-1, -2, 5, -11, 123, -55]
solution = (-55, 123)
output = get_min_max(input)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - one negative number")
input = [-5238559573295]
solution = (-5238559573295, -5238559573295)
output = get_min_max(input)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")