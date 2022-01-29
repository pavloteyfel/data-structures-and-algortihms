"""Write a function, tree_sum, that takes in the root of a binary tree that contains 
number values. The function should return the total sum of all values in the tree."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def tree_sum(root):
    if not root:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)


assert (tree_sum(a)) == 21
