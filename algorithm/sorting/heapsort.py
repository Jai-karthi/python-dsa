def max_heapify(A, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        print(largest,i)
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, heap_size, largest)
def min_heap(A,heap_size,i):
    left = 2 * i + 1
    right = 2 * i + 2
    small = i
    if left < heap_size and A[left] < A[small]:
        small = left
    if right < heap_size and A[right] < A[small]:
        small = right
    if small != i:
        A[i], A[small] = A[small], A[i]
        max_heapify(A, heap_size, small)
def min_heap(A,heap_size,i):
    left = 2 * i + 1
    right = 2 * i + 2
    small = i
    if left < heap_size and A[left] < A[small]:
        small = left
    if right < heap_size and A[right] < A[small]:
        small = right
    if small != i:
        A[i], A[small] = A[small], A[i]
        max_heapify(A, heap_size, small)
        
def build_heap(A):
    heap_size = len(A)
    for i in range (heap_size - 1 , -1,-1):
        # max_heapify(A,heap_size, i)
        min_heap(A,heap_size,i)
# [16, 14, 7, 10, 8, 2, 1, 4, 9, 3]
def heapsort(A):
    heap_size = len(A)
    build_heap(A)
    print(A)
    #print A #uncomment this print to see the heap it builds
    for i in range(heap_size-1,0,-1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, heap_size, 0)

A = [2,8,1,4,14,7,16,10,9,3]
heapsort(A)
print (A)
