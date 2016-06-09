class Node(object):
    def __init__(self, val):
        self.val = val
        self.next_node = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        else:
            self.head = new_node

    def insert_first(self, new_node):
        new_node.next_node = self.head
        self.head = new_node
        
    def delete_first(self):
        if self.head:
            deleted = self.head
            temp = deleted.next_node
            self.head = temp
            return deleted
        else:
            return None
            
class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()
    
