#Exercise 3

###Explanation
The intuition to solve this challenge is to alternating add one of the digits to a number,
while the number is multiplied by 10^x with x being the number of rounds a digit was added to
both numbers. x is starting by 0.
A really good datastructure for this is a heap. Therefore I implemented a heap, 
which offers
O(n log n) for sorting and O(1) for popping off the max element.

###Time Complexity
O(n log n)

###Space complexity
O(n)
