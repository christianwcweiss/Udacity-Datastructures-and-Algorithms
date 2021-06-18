'''
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit.
If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache.
If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element.
After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache.
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.
For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element.
If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
'''

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
