class Node:
    def __init__(self):
        self.key = 0
        self.prev = None
        self.next = None

class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_front(self, n):
        new_node = Node()

        new_node.key = n

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = self.head.prev

    def insert_back(self, n):
        new_node = Node()
        
        new_node.key = n

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    

    def delete_front(self):
        if self.head is None:
            return -1
        
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        
        r = node.key
        return r
    
    def delete_back(self):
        if self.tail is None:
            return -1

        node = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        
        r = node.key
        return r

    def insert_k(self, k, n):
        if k <= 0:
            return -1
        elif k is 1:
            self.insert_front(n)
        else:
            node = self.head

            for i in range(k-2):
                node = node.next
                if node is None:
                    self.insert_back(n)
                    return
            
            new_node = Node()
            new_node.key = n

            new_node.prev = node
            new_node.next = node.next

            node.next = new_node
            new_node.next.prev = new_node

deq = Dequeue()

deq.insert_front(3)
deq.insert_front(2)
deq.insert_front(1)

deq.insert_back(5)
deq.insert_back(6)

deq.insert_k(4, 4)
deq.insert_k(1, 0)
deq.insert_k(10, 8)
deq.insert_k(8, 7)

for i in range(4):
    print(deq.delete_back())

for i in range(5):
    print(deq.delete_front())
