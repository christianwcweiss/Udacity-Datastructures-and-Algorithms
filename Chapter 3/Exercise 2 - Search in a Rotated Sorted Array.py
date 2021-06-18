def find_pivot(input_list: list) -> int:
    l = 0
    h = len(input_list) - 1
    if input_list[0] < input_list[-1]:
        return 0
    while l < h:
        mid_index = (h + l) // 2
        if input_list[mid_index] < input_list[mid_index - 1]:
            return mid_index
        elif input_list[mid_index] > input_list[0]:
            l = mid_index
        elif input_list[mid_index] < input_list[-1]:
            h = mid_index

def rotated_array_search(input_list, number):
    '''
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    '''
    if input_list == []:
        return -1
    if not input_list or not number:
        return -1
    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1

    pivot = find_pivot(input_list)
    n = len(input_list)

    if number < input_list[pivot] or number > input_list[(pivot + n - 1) % n]:
        return -1
    l = 0
    h = n - 1
    while l <= h:
        mid_index = ((h+l) // 2)
        mid_index_pivot = (mid_index + pivot) % n
        if input_list[mid_index_pivot] == number:
            return mid_index_pivot
        elif input_list[mid_index_pivot] < number:
            l = mid_index + 1
        elif input_list[mid_index_pivot] > number:
            h = mid_index
    return -1


def linear_search(input_list, number):
    if not input_list or not number:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    output = rotated_array_search(input_list, number)
    print(output)
    if linear_search(input_list, number) == output:
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

#own test_cases
print("Test Case 1 - empty array")
input_list = []
number = 123
solution = linear_search(input_list, number)
output = rotated_array_search(input_list, number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - input_list None")
input_list = None
number = 123
solution = linear_search(input_list, number)
output = rotated_array_search(input_list, number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - number == None")
input_list = [3, 1, 2]
number = None
solution = linear_search(input_list, number)
output = rotated_array_search(input_list, number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - input_list not rotated")
input_list = [1, 2, 3, 4, 5, 6, 7]
number = 5
solution = linear_search(input_list, number)
output = rotated_array_search(input_list, number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - number too small")
input_list = [4, 5, 6, 7, 1, 2, 3]
number = -1
solution = linear_search(input_list, number)
output = rotated_array_search(input_list, number)
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
