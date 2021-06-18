d = {} #user, set_of_groups

class Group(object):

    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        for user in group.users:
            if user in d.keys():
                self.add_user(user)
        self.groups.append(group)

    def add_user(self, user):
        if user in d.keys():
            d[user].add(self.name)
        else:
            d[user] = set([self.name])
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user not in d.keys():
        return False
    else:
        return group.name in d[user]

print(is_user_in_group(sub_child_user, sub_child))
print(is_user_in_group(sub_child_user, child))
print(is_user_in_group(sub_child_user, parent))
print(is_user_in_group("this one doesn't exist", parent))

#own test_cases
print("Test Case 1 - group not existing")
solution = False
output = is_user_in_group("no user at all", child)
print(output)
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - subchild in parent")
solution = True
output = is_user_in_group(sub_child_user, parent)
print(output)
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - user not in group")
solution = False
new_group = Group("The cool group")
output = is_user_in_group(sub_child_user, new_group)
print(output)
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
