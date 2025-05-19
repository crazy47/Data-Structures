class stack:
    def __init__(self):
        self.stack_list = []  
    def push(self, value):
        self.stack_list.append(value) 
    def pop(self): 
        return self.stack_list.pop() if self.stack_list != 0 else None
    def peek(self): 
        return None if len(self.stack_list) == 0 else self.stack_list[-1] 
    def size(self): 
        return len(self.stack_list) 
    
s = stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.size())

