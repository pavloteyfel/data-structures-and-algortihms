import unittest
import pdb

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTIterative:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        current = self.root

        while current:
            if current.value > value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return

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
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)

            if root.value > value:
                root.left = _insert(root.left, value)
            
            if root.value < value:
                root.right = _insert(root.right, value)
            
            return root

        self.root =_insert(self.root, value)


    def search(self, value):
        def _search(root, value):
            if root:
                if root.value == value:
                    return root

                if root.value > value:
                    return _search(root.left, value)

                if root.value < value:
                    return _search(root.right, value)
            
            return None
        
        return _search(self.root, value)

    def delete(self, value):
        pass

    def traverse_in(self):
        results = []
        def _traverse(root):
            if root:
                _traverse(root.left)
                results.append(root.value)
                _traverse(root.right)
        
        _traverse(self.root)
        return results

    def traverse_pre(self):
        pass

    def traverse_past(self):
        pass

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bsti = BSTIterative()
        self.bstr = BSTRecursive()
        self.bstr.insert(15)
        self.bstr.insert(21)
        self.bstr.insert(9)
        self.bstr.insert(11)
        self.bstr.insert(5)
        self.bstr.insert(13)
        self.bstr.insert(33)
        self.bstr.insert(48)
        self.bstr.insert(19)
        self.bstr.insert(30)
        self.bsti.insert(15)
        self.bsti.insert(21)
        self.bsti.insert(9)
        self.bsti.insert(11)
        self.bsti.insert(5)
        self.bsti.insert(13)
        self.bsti.insert(33)
        self.bsti.insert(48)
        self.bsti.insert(19)
        self.bsti.insert(30)
    
    def test_insert_iterative(self):
        self.assertEqual(self.bsti.root.value, 15)
        self.assertEqual(self.bsti.root.left.value, 9)
        self.assertEqual(self.bsti.root.left.left.value, 5)
        self.assertEqual(self.bsti.root.left.right.value, 11)
        self.assertEqual(self.bsti.root.left.right.right.value, 13)
        self.assertEqual(self.bsti.root.right.value, 21)
        self.assertEqual(self.bsti.root.right.left.value, 19)
        self.assertEqual(self.bsti.root.right.right.value, 33)
        self.assertEqual(self.bsti.root.right.right.left.value, 30)
        self.assertEqual(self.bsti.root.right.right.right.value, 48)

    def test_insert_recursive(self):
        self.assertEqual(self.bstr.root.value, 15)
        self.assertEqual(self.bstr.root.left.value, 9)
        self.assertEqual(self.bstr.root.left.left.value, 5)
        self.assertEqual(self.bstr.root.left.right.value, 11)
        self.assertEqual(self.bstr.root.left.right.right.value, 13)
        self.assertEqual(self.bstr.root.right.value, 21)
        self.assertEqual(self.bstr.root.right.left.value, 19)
        self.assertEqual(self.bstr.root.right.right.value, 33)
        self.assertEqual(self.bstr.root.right.right.left.value, 30)
        self.assertEqual(self.bstr.root.right.right.right.value, 48)
    
    def test_search_recursive(self):
        self.assertEqual(self.bstr.search(33).value, 33)
        self.assertEqual(self.bstr.search(19).value, 19)
        self.assertFalse(self.bstr.search(99))
    
if __name__ == '__main__':
    unittest.main()