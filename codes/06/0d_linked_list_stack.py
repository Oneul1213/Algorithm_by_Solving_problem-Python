class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_front(self, data):
        new_node = Node()
        new_node.data = data

        if self.head == None:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        
        self.head = new_node
    
    def insert_back(self, data):
        new_node = Node()
        new_node.data = data

        if self.tail == None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        
        self.tail = new_node
    
    def pop_front(self):
        del_node = self.head

        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return del_node
    
    def pop_back(self):
        del_node = self.tail

        if self.tail.prev == None:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev

        return del_node

class Dl_StackUnderflowException(Exception):
    def __init__(self):
        super().__init__('Dl_Stack Underflow')

class Dl_Stack:
    def __init__(self):
        self.dl = DoublyLinkedList()
        self.top = self.dl.tail
    
    def push(self, data):
        self.dl.insert_back(data)
        self.top = self.dl.tail
    
    def pop(self):
        if self.top == None:
            raise Dl_StackUnderflowException
        del_data = self.dl.pop_back().data
        self.top = self.dl.tail

        return del_data

if __name__ == '__main__':
    # DoublyLiknedList 확인
    print('DoublyLinkedList Test')
    dl = DoublyLinkedList()
    dl.insert_back(1)
    dl.insert_front(3)
    dl.insert_back(5)
    dl.insert_front(2)
    # 2315
    del_val = dl.pop_back()
    # 231

    print(f'deleted: {del_val.data}')
    print(f'head: {dl.head.data}')
    print(f'tail: {dl.tail.data}')

    print()
    print('Dl Stack Test')
    # Dl_Stack 확인
    dls = Dl_Stack()
    dls.push(5)
    dls.push(4)
    dls.push(3)
    dls.push(2)
    dls.push(1)

    for i in range(5):
        print(f'pop {i} : {dls.pop()}')
    
    try:
        dls.pop()
    except Exception as e:
        print(f'Error: {e}')
