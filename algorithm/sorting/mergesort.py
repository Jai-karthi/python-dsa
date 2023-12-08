def merge_sort(list: [int]):
    list_length = len(list)
    
    if list_length == 1:
        return list
    
    mid_point = list_length // 2
    
    left_half = merge_sort(list[:mid_point])
    right_half = merge_sort(list[mid_point:])
    
    return merge(left_half, right_half)
    
def merge(left, right):
    output = []
    i = j = 0
    
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            output.append(left[i])
            i +=1
        else:
            output.append(right[j])
            j +=1
    output.extend(left[i:])
    output.extend(right[j:])
    
    return output
    
unsorted_list = [2, 4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
sorted_list = merge_sort(unsorted_list)
print(unsorted_list)
print(sorted_list)
