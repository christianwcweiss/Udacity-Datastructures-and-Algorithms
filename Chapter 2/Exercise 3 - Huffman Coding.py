import sys

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_characters(data: str) -> dict:
    result = {}
    for c in data:
        if c in result.keys():
            result[c] += 1
        else:
            result[c] = 1
    return result

def huffman_encoding(data: str):
    #First, determine the frequency of each character in the message
    if data == "":
        return "", None
    data_dict = count_characters(data)
    if len(data_dict) == 1:
        c = data_dict.get(data[0])
        tree = Tree(c)
        tree.left = data[0]
        encoded_data = data.replace(data[0], "0")
        return encoded_data, tree
    data_dict = sorted(data_dict.items(), key=lambda x: x[1])
    counter = 0
    root = None
    curr_node = None
    for k, v in data_dict:
        if not root:
            root = Node(k, v)
            curr_node = root
        else:
            curr_node.next = Node(k, v)
            curr_node = curr_node.next
        counter += 1

    while counter > 2:
        node_a = root
        node_b = root.next
        root = node_b.next
        counter -= 1
        tree = Tree(node_a.value + node_b.value)
        tree.left = node_a.key
        tree.right = node_b.key
        curr_node = root
        if tree.value < root.value:
            tree_node = Node(tree, tree.value)
            tree_node.next = root
            root = tree_node
        else:
            while curr_node:
                if not curr_node.next or tree.value < curr_node.next.value:
                    tree_node = Node(tree, tree.value)
                    tree_node.next = curr_node.next
                    curr_node.next = tree_node
                    break
                else:
                    curr_node = curr_node.next
    node_a = root
    node_b = root.next
    tree = Tree(node_a.value + node_b.value)
    tree.left = node_a.key
    tree.right = node_b.key

    code_dict = {}

    st = [(tree, "")]
    while st:
        element, code = st.pop()
        if isinstance(element, Tree):
            st.append((element.left, code + "0"))
            st.append((element.right, code + "1"))
        else:
            code_dict[element] = code
    encoded_data = []
    for c in data:
        encoded_data.append(code_dict[c])
    encoded_data = "".join(encoded_data)
    return encoded_data, tree

def huffman_decoding(data, tree):
    if data == "":
        return ""
    decoded_data = []
    root = tree
    curr_tree_node = root
    for c in data:
        if c == "0":
            if isinstance(curr_tree_node.left, str):
                decoded_data.append(curr_tree_node.left)
                curr_tree_node = root
            else:
                curr_tree_node = curr_tree_node.left
        if c == "1":
            if isinstance(curr_tree_node.right, str):
                decoded_data.append(curr_tree_node.right)
                curr_tree_node = root
            else:
                curr_tree_node = curr_tree_node.right

    decoded_data = "".join(decoded_data)
    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    #a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(encoded_data)
    print(tree)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

#own test_cases
print("Test Case 1 - empty string")
solution = ""
encoded_data, tree = huffman_encoding(solution)
assert(encoded_data == "")
output = huffman_decoding(encoded_data, tree)
print(output)
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - scrambled string from example")
solution = "The word is the bird"
encoded_data, tree = huffman_encoding(solution)
assert(encoded_data == "0110111011111100111100000000111001010011101010111011111101011010000001")
output = huffman_decoding(encoded_data, tree)
print(output)
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - unique characters")
solution = "abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
encoded_data, tree = huffman_encoding(solution)
assert(encoded_data == "0001000001010001100001110010000010010010100010110011000011010011100011110100000100010100100100110101000101010101100101110110000110010110100110110111000111010111100111111000001000011000101000111001001001011001101001111010001010011010101010111011001011011011101011111100001100011100101100111101001101011101101101111110001110011110101110111111001111011111101111110000000001")
output = huffman_decoding(encoded_data, tree)
print(output)
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - only one character")
solution = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
encoded_data, tree = huffman_encoding(solution)
assert(encoded_data == "000000000000000000000000000000000000000000")
output = huffman_decoding(encoded_data, tree)
print(output)
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - two different chars character")
solution = "AB"
encoded_data, tree = huffman_encoding(solution)
assert(encoded_data == "01")
output = huffman_decoding(encoded_data, tree)
print(output)
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))