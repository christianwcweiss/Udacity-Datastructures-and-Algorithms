
class Node(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.previous = None
        self.next = None

    def __repr__(self):
        return str(self.value)

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.root = None
        self.tail = None
        if capacity is not None:
            self.capacity = capacity
        else:
            self.capacity = capacity + 1





        self.cache = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache.keys():
            return -1
        node = self.cache[key]
        prev_node = node.previous
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.previous = prev_node
        elif prev_node:
            if node == self.tail:
                self.tail = prev_node
                prev_node.next = None
        elif next_node:
            if node == self.root:
                self.root = next_node
                next_node.previous = None
        del self.cache[key]
        return node.value

    def set(self, key, value):
        if key in self.cache.keys():
            print("Key already added to cache")
            return

        new_node = Node(key, value)
        if not self.root and not self.cache:
            self.root = new_node
            self.tail = new_node
            self.cache[key] = new_node
        elif len(self.cache) < self.capacity:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.cache[key] = new_node
        else:
            del self.cache[self.root.key]
            self.root = self.root.next
            self.cache[key] = new_node
            self.tail.next = new_node
            self.tail = self.tail.next



our_cache = LRU_Cache(5)

print("------------------")
print("our_cache.set(1, 1)")
our_cache.set(1, 1)
print(our_cache.cache)
print("------------------")
print("our_cache.set(2, 2)")
our_cache.set(2, 2)
print(our_cache.cache)
print("------------------")
print("our_cache.set(3, 3)")
our_cache.set(3, 3)
print(our_cache.cache)
print("------------------")
print("our_cache.set(4, 4)")
our_cache.set(4, 4)
print(our_cache.cache)
print("------------------")
print("our_cache.get(1) ")
our_cache.get(1)     # returns 1
print(our_cache.cache)
print("------------------")
print("our_cache.get(2)")
print(our_cache.get(2) == 2)       # returns 2
print(our_cache.cache)
print("------------------")
print("our_cache.get(9)")
print(our_cache.get(9) == -1)     # returns -1 because 9 is not present in the cache
print(our_cache.cache)
print("------------------")
print("our_cache.set(5, 5)")
our_cache.set(5, 5)
print(our_cache.cache)
print("------------------")
print("our_cache.set(6, 6)")
our_cache.set(6, 6)
print(our_cache.cache)
print("Added two more set operations, since my LRU is popping from the cache.")
print("------------------")
print("our_cache.set(7, 7)")
our_cache.set(7, 7)
print(our_cache.cache)
print("------------------")
print("our_cache.set(8, 8)")
our_cache.set(8, 8)
print(our_cache.cache)
print("------------------")
print("our_cache.get(3) ")
print(our_cache.get(3) == -1)     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.cache)

new_cache = LRU_Cache(capacity=3)

#own test_cases
print("Test Case 1 - get from empty cache")
solution = -1
output = new_cache.get(4)
print(output)
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - add until one item is removed")
solution = -1
new_cache.set(1, 1)
new_cache.set(2, 2)
new_cache.set(3, 3)
new_cache.set(4, 4)
output = new_cache.get(1)
print(output)
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - retreive value for key")
solution = 4
output = new_cache.get(4)
print(output)
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - capacity 0")
cond_1 = LRU_Cache(capacity=0)
cond_1.set(1, 1)
cond_1.set(2, 2)
solution = -1
output = cond_1.get(1)
print(output)
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - capacity None")
cond_2 = LRU_Cache(capacity=None)
cond_2.set(1, 1)
cond_2.set(2, 2)
solution = 2
output = cond_2.get(2)
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
