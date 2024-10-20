class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_ending(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def length_of_ll(self):
        count = 0
        itr = self.head
        while itr.next:
            itr = itr.next
            count += 1
        return count

    def insert_values(self, data):
        self.head = None
        for item in data:
            self.insert_at_ending(item)
    
    def insert_at(self, data, index):
        if index < 0 or index > self.length_of_ll():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_begining(data, self.head)
            return
        else:
            itr = self.head
            count = 0
            while itr.next:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                itr = itr.next
                count += 1
    
    def remove_at(self, index):
        if index < 0 or index > self.length_of_ll():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
        return
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['vinod', 'kumar', 'arjun', 'mouni'])
    ll.print()
    ll.insert_at('raghava', 2)
    ll.print()
    ll.remove_at(2)
    ll.remove_at(22)
    ll.print()
