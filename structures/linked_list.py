class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'Node({self.value})'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __repr__(self):
        return str(list(self.traverse()))
    
    def traverse(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def get(self, index):
        current = self.head
        counter = 0
        while index != counter:
            current = current.next
            counter += 1
        return current

    
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        self.tail.next = node
        self.tail = node
        self.size += 1


ll = LinkedList()
ll.append(3)
ll.append(2)
ll.append(6)
ll.append(3)
ll.append(9)
print(ll.get(4))