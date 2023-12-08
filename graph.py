class graph:
    def __init__(self):
        self.numberofnodes = 0
        self.edges = {}
        
    def insert(self,value):
        self.edges[value] = []
        self.numberofnodes += 1
        
    def connect(self,node1,node2):
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)
        print(self.edges)
my = graph()
my.insert("0")
my.insert("1")
my.insert("2")
my.insert("3")
my.insert("4")
my.insert("5")
my.insert("6")
my.connect("3","1")
my.connect("3","4")
my.connect("4","2")
my.connect("4","5")
my.connect("1","2")
my.connect("1","0")
my.connect("0","2")
my.connect("6","5")
print(my)