import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTIterative:
    def insert(self, value):
        pass

    def search(self, value):
        pass

    def delete(self, value):
        pass

    def traverse_in(self):
        pass

    def traverse_pre(self):
        pass

    def traverse_past(self):
        pass


class BSTRecursive:
    def insert(self, value):
        pass

    def search(self, value):
        pass

    def delete(self, value):
        pass

    def traverse_in(self):
        pass

    def traverse_pre(self):
        pass

    def traverse_past(self):
        pass

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bsti = BSTIterative()
        self.bstr = BSTRecursive()

if __name__ == '__main__':
    unittest.main()