class Queue:
    def __init__(self, front=None):
        self.q = [front]

    def enqueue(self, new_entity):
        self.q.append(new_entity)

    def first(self):
        return self.q[0] 

    def dequeue(self):
        return self.q.pop(0)
    
