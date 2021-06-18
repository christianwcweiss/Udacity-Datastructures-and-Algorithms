## Exercise 3

Data Structures:
I used again a linked list. And a tree.
I used the linked list to make use of the easy to implement insertion and removing operation.
Therefore I didn't need to sort anything, just efficiently insert.
I used the tree because in the end I should gain a tree for the en/decoding.
I used a dictionary to store the occurences. I use an built-in sorting function which is the timsort in Python,
which has O(nlogn) complexity, with n being the number of items in the dictionary. However, since I save the occurences and if I assume,
only alphabet, numeric and a small amount of special characters are used,
n won't exceed 100, which keeps the initial sorting very fast.

Time complexity:
create dictionary -> O(n), with n being characters in the data_string
sort dictionary -> O(mlogm), with m being the unique characters in the string.
This can be worst case the length of the input data.
- generating tree -> O(m) 
- for outer loop + O(m) (worst-case) 
- for inserting back to the linked list
- generating code dictionary -> O(m)
- generating code made of 0 and 1 -> O(n)

Space complexity:
O(m) with m being unique characters in the input data
- If the input string is long the space complexity is actually reduced.
- If the input string has only unique characters the space complexity goes up, because
I need to save the code.

