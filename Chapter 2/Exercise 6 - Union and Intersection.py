class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    union_set = set([])
    res_llist = LinkedList()

    curr_node = llist_1.head
    while curr_node:
        if curr_node.value not in union_set:
            union_set.add(curr_node.value)
            res_llist.append(curr_node.value)
        curr_node = curr_node.next

    curr_node = llist_2.head
    while curr_node:
        if curr_node.value not in union_set:
            res_llist.append(curr_node.value)
        curr_node = curr_node.next

    return res_llist


def intersection(llist_1, llist_2):
    intersection_set = set([])

    res_llist = LinkedList()

    curr_node = llist_1.head
    while curr_node:
        intersection_set.add(curr_node.value)
        curr_node = curr_node.next

    curr_node = llist_2.head
    while curr_node:
        if curr_node.value in intersection_set:
            res_llist.append(curr_node.value)
        curr_node = curr_node.next

    return res_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Union")
print (union(linked_list_1,linked_list_2))
print("Intersection")
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Union")
print (union(linked_list_3,linked_list_4))
print("Intersection")
print (intersection(linked_list_3,linked_list_4))

#own test_cases
print("Test Case 1 - empty linked list intersect")
solution = None
ll_1 = LinkedList()
ll_2 = LinkedList()

element_1 = [1, 2, 3]
element_2 = [4, 5, 6]

for i in element_1:
    ll_1.append(i)

for i in element_2:
    ll_2.append(i)
output = intersection(ll_1, ll_2)
print(output)
assert(output.head == None)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output.head, solution))
print("---------------------------")
print("Test Case 2 - six elements in result - union")
solution = "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> "
output = union(ll_1, ll_2)
print(output)
assert(str(output) == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - one list empty union ")
ll_1 = LinkedList()
ll_2 = LinkedList()

element_1 = [1, 2, 3]
element_2 = []

for i in element_1:
    ll_1.append(i)

for i in element_2:
    ll_2.append(i)
output = union(ll_1, ll_2)
print(output)
assert(str(output) == str(ll_1))
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - union")
solution = "1 -> 2 -> 3 -> 4 -> "
ll_1 = LinkedList()
ll_2 = LinkedList()

element_1 = [1, 2, 3]
element_2 = [2, 3, 4]

for i in element_1:
    ll_1.append(i)

for i in element_2:
    ll_2.append(i)
output = union(ll_1, ll_2)
print(output)
assert(str(output) == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")

print("Test Case 5 - intersection")
solution = "2 -> 3 -> 4 -> "
ll_1 = LinkedList()
ll_2 = LinkedList()

element_1 = [1, 2, 3, 4, 5, 6]
element_2 = [2, 3, 4, 7, 8, 9, 10]

for i in element_1:
    ll_1.append(i)

for i in element_2:
    ll_2.append(i)
output = intersection(ll_1, ll_2)
print(output)
assert(str(output) == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 6 - intersection both lists empty")
solution = ""
ll_1 = LinkedList()
ll_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    ll_1.append(i)

for i in element_2:
    ll_2.append(i)
output = intersection(ll_1, ll_2)
print(output)
assert(str(output) == solution)
print("TestCase 6 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 7 - union both lists empty")
solution = ""
ll_1 = LinkedList()
ll_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    ll_1.append(i)

for i in element_2:
    ll_2.append(i)
output = union(ll_1, ll_2)
print(output)
assert(str(output) == solution)
print("TestCase 7 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")