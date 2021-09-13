# Find the max element 
# Initialize an array with length = max element + 1 to store element counts 
# Initialize output array 
# Store counts of each element from the input array in counts array (use: index = element, ie counts[element] += 1)
# Get a cumulative sum array for finding sorted array indices of elements in input array 
# Loop through input array 
# Get element count from cum_sum_array (use: index = element, i.e cum_sum_array[element])
# Set sorted index or element = element_count - 1 
# Place element in correct spot in output array 
# Decrease count of element in cum_sum_array by 1 (use: index = element, i.e cum_sum_array[element])
# Return output array 

from utils import * 

def counting_sort(arr):
    max_element = max(arr)
    counts = [0 for i in range(max_element + 1)]
    output = [0 for i in range(len(arr))]

    for i in arr: 
        counts[i] += 1
    cum_sum_arr = cum_sum(counts)
 
    for i in arr: 
        element_count = cum_sum_arr[i]
        sorted_index = element_count - 1
        output[sorted_index] = i
        cum_sum_arr[i] -= 1
    return output

if __name__ == '__main__':
    arr = [4,2,2,8,3,3,1]
    sorted_arr = counting_sort(arr)
    print(sorted_arr)
