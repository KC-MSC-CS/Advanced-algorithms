def heapify(arr,n,i):
    # initialize largest to root index 
    largest = i                 
    left_child = (i * 2) + 1
    right_child = (i * 2) + 2

    # if left child is greater than largest 
    if(left_child < n and arr[left_child] > arr[largest]):
        largest = left_child

    # if right child is greater than largest
    if(right_child < n and arr[right_child] > arr[largest]):
        largest = right_child

    # if largest is not the root 
    if(largest != i):
        # swap the root with the largest element 
        arr[i],arr[largest] = arr[largest],arr[i]
        # recursively heapify the affected sub tree 
        heapify(arr,n,largest)

def buildHeap(arr,n):
    # index of last non leaf node (i.e parent of last node)
    start_index = (n - 1) // 2 
    # start iterating through the input array in reverse order 
    for i in range(start_index,-1,-1):
        print(i)
        heapify(arr,n,i)
    return arr

def heap_sort(arr):
    arr_size = len(arr)
    heap = buildHeap(arr,arr_size)      # (n-1)(logn)
    # swap element at first position with element at last postion 
    # heapify the arr to maintain max-heap property 
    # repeat for all elements except the 
    for i in range(arr_size-1,0,-1):    # (n-1)(logn)
        arr[i],arr[0] = arr[0],arr[i]
        heapify(heap,i,0)               

    return arr 

if __name__ == '__main__':
    arr = [23,1234,3,10,34,2,1,23]
    arr = heap_sort(arr)
    print(arr)