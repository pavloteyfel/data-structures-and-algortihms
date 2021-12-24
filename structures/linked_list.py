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
            yield current.value
            current = current.next

    def get(self, index):
        if not (0 <= index < self.size):
            return None

        current = self.head
        counter = 0
        while index != counter:
            current = current.next
            counter += 1
        return current

    def pop(self):
        to_remove = self.tail

        if self.size < 2:
            self.head = self.tail = None
        else:
            previous = self.get(self.size - 2)
            previous.next = None
            self.tail = previous
        self.size -= 1
        return to_remove
    
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        self.tail.next = node
        self.tail = node
        self.size += 1
    
    def reverse(self):
        current = self.head
        while current.next:
            nxt = current.next
            nxt_nxt = current.next.next
            current.next = nxt_nxt
            nxt.next = self.head
            self.head = nxt
        self.tail = current



ll = LinkedList()
ll.append(3)
ll.append(2)
ll.append(6)
ll.append(3)
ll.append(9)

assert list(ll.traverse()) == [3, 2, 6, 3, 9]
assert ll.get(0).value == 3
assert ll.size == 5
assert ll.get(5) == None
ll.reverse()
assert list(ll.traverse()) == [9, 3, 6, 2, 3]
