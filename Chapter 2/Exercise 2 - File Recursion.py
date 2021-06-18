import os

def find_files(suffix, path):

    st = [path]
    result = []
    while st:
        path = st.pop()
        if not os.path.isdir(path):
            continue
        for directory in os.listdir(path):
            new_path = "{0}/{1}".format(path, directory)
            if directory.endswith(suffix):
                result.append(new_path)
                st.append(new_path)
            else:
                st.append(new_path)

    return result

print("Example Test Case - Udacity - Find .c")
print(find_files(".c", "testdir"))

#own test_cases
print("Test Case 1 - Find .h")
solution = ["testdir/subdir1/a.h", "testdir/subdir3/subsubdir1/b.h", "testdir/subdir5/a.h", "testdir/t1.h"]
output = find_files(".h", "testdir")
print(output)
assert(sorted(output) == sorted(solution))
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - Find .jpeg")
solution = []
output = find_files(".jpeg", "testdir")
print(output)
assert(sorted(output) == sorted(solution))
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - Find .jpeg")
solution = []
output = find_files(".jpeg", "testdir")
print(output)
assert(sorted(output) == sorted(solution))
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - Find subdir subdir3")
solution = ["testdir/subdir3"]
output = find_files("subdir3", "testdir")
print(output)
assert(sorted(output) == sorted(solution))
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - Find subdir subdir1")
solution = ["testdir/subdir1", "testdir/subdir3/subsubdir1"]
output = find_files("subdir1", "testdir")
print(output)
assert(sorted(output) == sorted(solution))
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))