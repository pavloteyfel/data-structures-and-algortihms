import abc

class Node:
    """Container for the binary search tree structure"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """This is the context class, a binary search tree"""
    def __init__(self):
        self.root = None
        self._insert_strategy = None

    def set_insert_strategy(self, strategy):
        self._insert_strategy = strategy
    
    def insert(self, value):
        self.root = self._insert_strategy.execute(self.root, value)



class Insert(abc.ABC):
    @abc.abstractmethod
    def execute(self, node, value):
        pass

class RecursiveInsert(Insert):
    def execute(self, node, value):
        if not node:
            return Node(value)
        if node.value > value:
            node.left = self.execute(node.left, value)
        else:
            node.right = self.execute(node.right, value)
        return node

class IterativeInsert(Insert):
    def execute(self, node, value):
        if not node:
            return Node(value)

        current = node
        while current:
            if current.value > value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return node
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    return node




bst = BST()
bst.set_insert_strategy(RecursiveInsert())

bst.insert(1)
bst.insert(10)

print(bst.root.value)
print(bst.root.right.value)

bst.set_insert_strategy(IterativeInsert())
bst.insert(1)
bst.insert(10)

print(bst.root.value)
print(bst.root.right.value)