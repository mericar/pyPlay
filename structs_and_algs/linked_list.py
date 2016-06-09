
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
            
    def get_position(self, position):
        curr = self.head
        acc = 1
        if position == acc:
            return curr
        else:
            while curr.next_node:
                curr = curr.next_node
                acc += 1
                if acc == position:
                    return curr
            return None
    
    def insert(self, new_node, pos):
        curr = self.head
        acc = 1
        if pos == acc:
            new_node = self.head
            curr = curr.next_node
        else:
            while curr.next_node:
                curr = curr.next_node
                acc += 1
                if (pos - 1) == acc:
                    temp = Element(0)
                    temp = curr.next_node
                    curr.next_node = new_element
                    new_node.next_node = temp
                    return
                    
    def delete(self, val):
        """Deletes the first node with a given value."""
        curr = self.head
        prev = Node(0)
        if curr.val == val:
            self.head = curr.next_node
        while curr.next_node:
            prev = curr
            curr = curr.next_node
            if curr.val == value:
                prev.next_node = curr
        return
                
                



