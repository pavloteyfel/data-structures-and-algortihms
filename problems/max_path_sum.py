"""Write a function, max_path_sum, that takes in the root of a binary tree that contains
number values. The function should return the maximum sum of any root to leaf path 
within the tree."""

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