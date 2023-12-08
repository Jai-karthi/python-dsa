class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
class binarytree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        newnode = Node(value)
        if self.root == None:
            self.root = newnode
        else:
            currentnode = self.root
            while (True):
                if value < currentnode.value:
                    if not currentnode.left:
                        currentnode.left = newnode
                        return self
                    currentnode = currentnode.left
                else:
                    if not currentnode.right:
                        currentnode.right = newnode
                        return self
                    currentnode = currentnode.right
                    
                    
    def bfs(self):
        currentnode = self.root
        listt = []
        queue = []
        queue.append(currentnode)
        while len(queue) > 0:
            currentnode = queue.pop()
            listt.append(currentnode.value)
            
            if currentnode.left:
                queue.append(currentnode.left)
            if currentnode.right:
                queue.append(currentnode.right)
                
        print(listt)
        
my = binarytree()
my.insert(9)
my.insert(4)
my.insert(6)
my.insert(20)
my.insert(170)
my.insert(1)
my.bfs()