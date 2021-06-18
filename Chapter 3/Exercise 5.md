# Exercise 5

### Explanation
I implemented a trie structure using a dictionary. The dictionary contains all 
lowercase alphabet characters. In case it's on a real productive environment,
special characters could be added easily, but it would make sense to also have the 
dictionary dynamic, i.e. any character can be added and only an entry in the dictionary
is made if the character was at least added ones.
I discarded characters that are not in the dictionary. This depends on the specification of the
project.

### Time Complexity
Finding all suffixes from a word depends on the length of the word and the number
of words already added.
k = number of words added
n = average length of words
then the worst case time complexity would be approximately O(k*n) for finding the
suffixes.
Inserting is O(1)

### Space complexity
Space complexity would be O(k*n) in the worst case.
The more words that are however, added, the less space it consumes since many
letter combinations would repeat in the trie. 
Example: "tree" and "trees". tree is the same in both words and to store "trees" 
only an additional "s" needs to be stored.
