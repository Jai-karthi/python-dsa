def selctionsort(array):
    for i in range(len(array)):
        mi = i
        temp = array[i]
        for j in range(i + 1,len(array)):
            if array[j] < array[mi]:
                mi = j
                
        array[i] = array[mi]
        array[mi] = temp
    return array
print(selctionsort([99,44,6,2,1,5,63,87,283,4,0]))