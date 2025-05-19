class queue: 
    def __init__(self):
        self.LIST = [] 
    def enqueue(self, val):  
        self.LIST = self.LIST + [val] 
        return None  
    def dequeue(self):
        return None if len(self.LIST) == 0 else self.LIST.pop(0)
    def front(self): 
        return None if len(self.LIST) == 0 else self.LIST[0] 
    def rear(self): 
        return None if len(self.LIST) == 0 else self.LIST[-1]
    def size(self): 
        return len(self.LIST)  

q = queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  
print(q.front())  
print(q.rear())  
print(q.size())   