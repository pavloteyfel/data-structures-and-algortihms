import unittest
import pdb

# Search: https://leetcode.com/problems/search-in-a-binary-search-tree/
# Delete: https://leetcode.com/problems/delete-node-in-a-bst/discuss/821420/Python-O(h)-solution-explained
# inorder traversal: https://leetcode.com/problems/binary-tree-inorder-traversal/
# todo: https://leetcode.com/problems/balanced-binary-tree/
# simpler post order with stack: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45786/Python-recursive-and-iterative-solutions.
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
        current = self.root
        while current:
            if current.value == value:
                return current

            elif current.value > value:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, value):
        pass

    def traverse_in(self):
        stack = []
        results = []
        current = self.root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                results.append(current.value)
                current = current.right
        return results
  
    def traverse_pre(self):
        results = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                results.append(node.value)
        return results

    def traverse_post(self):
        results = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                results.append(node.value)
                stack.append(node.left)
                stack.append(node.right)
        return results[::-1]


class BSTRecursive:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)

            elif root.value > value:
                root.left = _insert(root.left, value)
            
            else: # root.value < value
                root.right = _insert(root.right, value)
            
            return root

        self.root =_insert(self.root, value)


    def search(self, value):
        def _search(root, value):
            if not root:
                return

            if root.value == value:
                return root

            elif root.value > value:
                return _search(root.left, value)

            else:
                return _search(root.right, value)

        
        return _search(self.root, value)

    def delete(self, value):
        def _delete(root, value):
            if not root:
                return
            
            if root.value == value:
                if not root.right:
                    return root.left
                
                if not root.left:
                    return root.right

                # megeressük a jobb oldali érték legbaloldalibb értékét
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                
                root.value = tmp.value # itt a legbaloldalibb értékkel felülírjuk
                root.right = _delete(root.right, root.value) # itt pedig törlést kérünk

            elif root.value > value:
                root.left = _delete(root.left, value)
            else:
                root.right = _delete(root.right, value)

            
            return root


        return _delete(self.root, value)

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

    def traverse_post(self):
        pass

class TestBST(unittest.TestCase):
    def setUp(self):
        self.traverse_in = [5, 9, 11, 13, 15, 19, 21, 30, 33, 48]
        self.traverse_pre = [15, 9, 5, 11, 13, 21, 19, 33, 30, 48]
        self.traverse_post = [5, 13, 11, 9, 19, 30, 48, 33, 21, 15]
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
    
    def test_search_iterative(self):
        self.assertEqual(self.bsti.search(33).value, 33)
        self.assertEqual(self.bsti.search(19).value, 19)
        self.assertFalse(self.bsti.search(99))
    
    def test_traverse_in_iterative(self):
        self.assertEqual(self.bsti.traverse_in(), self.traverse_in)
    
    def test_traverse_pre_iterative(self):
        self.assertEqual(self.bsti.traverse_pre(), self.traverse_pre)
    
    def test_traverse_post_interative(self):
        self.assertEqual(self.bsti.traverse_post(), self.traverse_post)
    
    def test_delete_recursive(self):
        self.bstr.delete(21)
        
        self.assertEqual(self.bstr.traverse_in(), [5, 9, 11, 13, 15, 19, 30, 33, 48])
    
if __name__ == '__main__':
    unittest.main()