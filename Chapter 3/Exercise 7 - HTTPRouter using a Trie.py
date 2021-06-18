
class RouteTrieNode:
    def __init__(self, path, handler):
        self.path = path
        self.handler = handler
        self.sub_path = {}

class RouteTrie:
    def __init__(self, root_path, root_handler):
        self.root_node = RouteTrieNode(root_path, root_handler)

    def insert(self, path_list, handler):
        current_node = self.root_node
        for i, path in enumerate(path_list):
            if path in current_node.sub_path.keys():
                current_node = current_node.sub_path[path]
                if i == len(path_list) - 1:
                    old_handler = current_node.handler
                    current_node.handler = handler
                    print("Old handler *{0}* was overwritten by *{1}*".format(old_handler, handler))
            else:
                if i < len(path_list) - 1:
                    new_node = RouteTrieNode(path, None)
                else:
                    new_node = RouteTrieNode(path, handler)
                current_node.sub_path[path] = new_node
                current_node = new_node

    def find(self, path_list):
        current_node = self.root_node
        for path in path_list:
            if path in current_node.sub_path.keys():
                current_node = current_node.sub_path[path]
            else:
                return None

class Router:
    def __init__(self, root_path, root_handler, not_found_handler):
        self.route_trie = RouteTrie(root_path, root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_list = self.split_path(path)
        self.route_trie.insert(path_list, handler)

    def lookup(self, path):
        if self.route_trie.root_node.path == path:
            return self.route_trie.root_node.handler
        path = path.rstrip('/')
        path_list = self.split_path(path)
        current_node = self.route_trie.root_node
        for path in path_list:
            if path in current_node.sub_path.keys():
                current_node = current_node.sub_path[path]
            else:
                return self.not_found_handler
        return current_node.handler


    def split_path(self, s):
        return s.split('/')

router = Router("/", "root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/"))
print(router.lookup("/home"))
print(router.lookup("/home/about"))
print(router.lookup("/home/about/"))
print(router.lookup("/home/about/me"))
print("\n\n")

#own test_cases
print("Test Case 1 - create new router")
tc_router = Router("/", "home handler", "error 404 handler")
temp_node = RouteTrieNode("/", None)
solution = temp_node.path
output = tc_router.route_trie.root_node.path
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - add handler")
tc_router.add_handler("/home/about/test", "test handler")
solution = "test handler"
output = tc_router.lookup("/home/about/test")
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - lookup with / on the end")
solution = "test handler"
output = tc_router.lookup("/home/about/test/")
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - overwrite handler")
solution = "overwrite handler"
tc_router.add_handler("/home/about/test", "overwrite handler")
output = tc_router.lookup("/home/about/test/")
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - add new handler")
solution = "new handler"
tc_router.add_handler("/home/about/new", "new handler")
output = tc_router.lookup("/home/about/new/")
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 6 - lookup and return no handler")
solution = "error 404 handler"
output = tc_router.lookup("/home/about/this does not exist/")
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 6 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 7 - lookup home handler")
solution = "home handler"
output = tc_router.lookup("/")
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 7 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")