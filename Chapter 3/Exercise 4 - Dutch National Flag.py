def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not input_list:
        return []

    if len(input_list) == 0 or len(input_list) == 1:
        return input_list

    lo = 0
    hi = len(input_list) - 1
    i = 0
    while i <= hi:
        num = input_list[i]
        if num == 0:
            input_list[i] = input_list[lo]
            input_list[lo] = 0
            lo += 1
            i += 1
        elif num == 2:
            input_list[i] = input_list[hi]
            input_list[hi] = 2
            hi -= 1
        elif num == 1:
            i += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

#own test_cases
print("Test Case 1 - empty array")
input_list = []
solution = sorted(input_list)
output = sort_012(input_list)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - input_list None")
input_list = None
solution = []
output = sort_012(input_list)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - No 0 in array")
input_list = [1, 1, 2, 1, 2, 1, 2]
solution = sorted(input_list)
output = sort_012(input_list)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - No 1 in array")
input_list = [0, 0, 0, 0, 2, 2, 2, 0, 2, 0, 0]
solution = sorted(input_list)
output = sort_012(input_list)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - No 2 in array")
input_list = [0, 0, 1, 0, 0, 1, 1, 0, 1]
solution = sorted(input_list)
output = sort_012(input_list)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 6 - only 2 in array")
input_list = [2, 2, 2, 2]
solution = sorted(input_list)
output = sort_012(input_list)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 6 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")