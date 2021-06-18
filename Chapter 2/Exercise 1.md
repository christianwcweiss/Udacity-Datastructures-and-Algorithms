## Exercise 1

Data Structures:
I chose a double linked list and a dictionary for this exercise.
Alternatively to the linked list I could have also used an array,
since an array is built-in as a double linked list would work.
The exercise wants to store key-value pairs, with the twist, that
if it's full the oldest element gets removed.
Storing key-value pairs is straight forward -> Dictionary
The problem here is: 
- "What if an element in the middle gets removed?"
- "If I use another datastructure how do I guarantee O(1) in 
all operations?"
  
Therefore a doubled linked list felt good for me to use,
since if I want to add an element, it's in O(1) and removing is O(1) and retreiving is O(1)
if the value of the dictionary is pointing to the Node.

Time complexity:
O(1) all operations

Space complexity:
O(m * n) with m being the keys and n being the values
I think it can be reduced to O(n), with n being the items stored.

