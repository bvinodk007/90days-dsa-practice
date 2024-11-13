class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, item):
        node = Node(item, self.start, None)
        if self.start is not None:
            self.start.prev = node
        self.start = node

    def insert_at_end(self, item):
        node = Node(item)
        if self.is_empty():
            self.start = node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp.item
            temp = temp.next
        return False

    def insert_at_item(self, item, data):
        temp = self.start
        while temp is not None and temp.item != item:
            temp = temp.next
        if temp is not None:
            node = Node(data, temp.next, temp)
            if temp.next is not None:
                temp.next.prev = node
            temp.next = node

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    def delete_at_start(self):
        if self.start is None:
            return
        self.start = self.start.next
        if self.start is not None:
            self.start.prev = None
    
    def delete_at_end(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
    
    def delete_item(self, item):
        temp = self.start
        while temp is not None:
            if temp.item == item:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp == self.start:
                    self.start = temp.next
                return
            temp = temp.next

dll = DLL()
dll.insert_at_start(5)
dll.insert_at_start(10)
dll.insert_at_start(15)
dll.insert_at_end(20)
dll.print_list()

dll.delete_at_start()
dll.print_list()

dll.delete_at_end()
dll.print_list()

dll.delete_item(10)
dll.print_list()
