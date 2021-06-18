class MaxHeap():
    def __init__(self, l):
        self.heap = l
        self.heapify()

    def child_ids(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        return left, right

    def parent_ids(self, i):
        return (i - 1) // 2

    def heapify(self):
        for i in range(len(self.heap)-1, -1, -1):
            parent = self.parent_ids(i)
            if parent == -1:
                break
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

        print(self.heap)

    def pop(self):
        if self.heap == []:
            return None
        max_element = self.heap[0]
        self.heap = self.heap[1:]
        self.heapify()
        return max_element

    def peek(self):
        if self.heap == []:
            return None
        return self.heap[0]

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list or input_list == []:
        return [0, 0]
    max_heap = MaxHeap(input_list)
    n1 = 0
    n2 = 0
    round = 0
    while max_heap.peek():
        max_element = max_heap.pop()
        if round % 2 == 0:
            n1 = n1 * 10 + max_element
        else:
            n2 = n2 * 10 + max_element
        round += 1
    return [n1, n2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

print("Test Case 1 - empty array")
input_list = []
solution = 0
output = sum(rearrange_digits(input_list))
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - only 0s")
input_list = [0, 0, 0, 0]
solution = 0
output = sum(rearrange_digits(input_list))
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - 1, 2, 3, 4, 5, 6")
input_list = [1, 2, 3, 4, 5, 6]
solution = 1173 # 642 + 531
output = sum(rearrange_digits(input_list))
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
