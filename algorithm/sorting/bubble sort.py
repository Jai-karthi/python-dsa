l = [6,5,3,1,8,7,4]
for _ in range(len(l)):
    for j in range(len(l) -1):
        if l[j] > l[j + 1]:
            holding = l[j]
            l[j] =   l[j + 1]
            l[j + 1] = holding
            
print(l)