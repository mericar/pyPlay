
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        curr = self.head
        acc = 1
        if position == acc:
            return curr
        else:
            while curr.next:
                curr = curr.next
                acc += 1
                if acc == position:
                    return curr
            return None
    
    def insert(self, new_element, position):
        curr = self.head
        acc = 1
        if position == acc:
            new_element = self.head
            curr = curr.next
        else:
            while curr.next:
                curr = curr.next
                acc+=1
                if (position-1) == acc:
                    temp = Element(0)
                    temp = curr.next
                    curr.next = new_element
                    new_element.next = temp
                    return
                    
    def delete(self, value):
        """Delete the first node with a given value."""
        curr = self.head
        prev = Element(0)
        if curr.value == value:
            self.head = curr.next
        while curr.next:
            prev = curr
            curr = curr.next
            if curr.value == value:
                prev.next = curr
        return
                
                



