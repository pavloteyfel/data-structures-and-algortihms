import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTIterative:
    pass

class BSTRecursive:
    pass

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bsti = BSTIterative()
        self.bstr = BSTRecursive()

if __name__ == '__main__':
    unittest.main()