class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self, start=None):
        self.start=start
    
    def is_empty(self):
        return self.start==None
    
    def print_sll(self):
        temp = self.start
        while temp is not None:
            print(str(temp.item),end='-->')
            temp = temp.next
        print("None")
    
    def insert_at_start(self, data):
        node=Node(data, self.start)
        self.start = node

    def insert_at_end(self, data):
        node=Node(data,None)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=node
        else:
            self.start=node
    
    def search(self, data):
        temp=self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return False
    
    def insert_after(self, item, data):
        if item is not None:
            node=Node(data, item.next)
            item.next=node
    
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    
    def delete_end(self):
        if self.start is None:
            pass
        else:
            if self.start.next is None:
                self.start = None
                return
            temp = self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def delete_item(self, item):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == item:
                self.start=None
        else:
            temp=self.start
            if temp.item==item:
                self.start=temp.next
                return
            else:
                while temp.next is not None:
                    if temp.next.item==item:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

sll = SLL()
sll.insert_at_start(9)
sll.insert_at_start(10)
sll.insert_at_start(5)
sll.insert_at_end(8)
sll.insert_at_end(43)
sll.insert_at_end(51)
sll.insert_at_end(90)
sll.insert_after(sll.search(51), 74)
for x in sll:
    print(x,end=" ")