class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
        
class binarysearchtree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        newnode = Node(value)
        if self.root == None:
            self.root = newnode
            return self.root.value
            
        else:
            current = self.root
            while True:
                if value < current.value:
                    if not current.left:
                        current.left = newnode
                        return current.left.value
                    current = current.left
                else:
                    if not current.right:
                        current.right = newnode
                        return current.right.value
                    current = current.right
                    
    def lookup(self,value):
        current = self.root
        if (current.value == None):
            return False
        while(current):
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            elif current.value == value:
                return current.value
        return False

my = binarysearchtree()
my.insert(9)
my.insert(8)
my.insert(10)

print(my.lookup(10))