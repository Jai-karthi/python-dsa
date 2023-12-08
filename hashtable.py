hashtable = [[],] * 10

def _hash(key):
    hassh = 0
    for i in key:
        hassh = (hassh +  ord(i)) % 2
        
    return hassh
    
def insertdata(key,data):
    index = _hash(key)
    if not hashtable[index]:
        hashtable[index] = []
        hashtable[index].append([key,data])
    else:
        hashtable[index].append([key,data])
        
    return hashtable
    
def removedata(key):
    removenode = _hash(key)
    bucket = hashtable[removenode]
    print(bucket)
    for i in range(len(bucket)):
        if bucket[i][0] == key:
            bucket[i] = 0 
        
insertdata("kjdfhf",1234213)
insertdata("kl",121345)
insertdata("sddkfdsmkfhf",14313)
insertdata("dfsfdkjdfhf",71213)
removedata("kl")
removedata("dfsfdkjdfhf")
removedata("kjdfhf")
print(hashtable)