# Exercise 7

### Explanation
To store the subpaths I used a dictionary, because it allows lookup in O(1) time
and I can store the values for a key, which are the nodes in my case.

### Time Complexity
n = number of path elements after spliting up by slash '/'
insert O(n)
find O(n)

### Space complexity
k = number of unique elements
O(k*n)
