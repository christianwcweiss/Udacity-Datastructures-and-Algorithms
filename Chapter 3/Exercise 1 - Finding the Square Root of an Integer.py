def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return -1
    if number == 0:
        return 0
    if number == 1:
        return 1

    l = 1
    h = number
    while l < h:
        mid_index = (h+l) // 2
        square = mid_index * mid_index
        next_square = (mid_index + 1) * (mid_index + 1)
        if (square < number and next_square > number) or square == number:
            return mid_index
        elif square < number:
            l = mid_index
        elif square > number:
            h = mid_index


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

#own test_cases
print("Test Case 1 - number == 0")
number = 0
solution = 0
output = sqrt(number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - number == negative")
number = -5
solution = -1
output = sqrt(number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - number == 1")
number = 1
solution = 1
output = sqrt(number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - number == positive even")
number = 36
solution = 6
output = sqrt(number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - number == positive even")
number = 11
solution = 3
output = sqrt(number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
