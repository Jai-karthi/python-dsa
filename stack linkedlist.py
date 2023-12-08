class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def peak(self):
        return self.top
        
    def push(self,value):
        newnode = node(value)
        if self.length == 0:
            self.top = newnode
            self.bottom = newnode
        else:
            holding = self.top
            self.top = newnode
            self.top.next = holding
        self.length += 1
        
    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
            
        holding = self.top
        self.top = self.top.next
        self.length -= 1
        print(self.length)
my = stack()
my.push("google")
my.push("apple")
my.push("facebook")
my.push("netflix")
my.pop()