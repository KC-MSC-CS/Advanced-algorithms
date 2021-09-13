def get_digit(num,place):
    return int((num/place) % 10)

def num_digits(num):
    digit_count = 0
    while(num != 0):
        digit_count += 1
        num //= 10
    return digit_count
    
def cum_sum(arr):
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    return arr 

def counting_sort(arr,place):
    arr_size = len(arr)
    output = [0] * arr_size
    counts = [0] * 10  # length of counts is 10 because at every iteration elements of arr will be single digit 

    for i in range(arr_size):
        digit = get_digit(arr[i],place)  # gets the digit at place from number 
        counts[digit] += 1 
    counts = cum_sum(counts)

    for i in reversed(range(arr_size)): 
        digit = get_digit(arr[i],place) 
        sorted_index = counts[digit] - 1
        output[sorted_index] = arr[i]
        counts[digit] -= 1
    return output 

def radix_sort(arr):
    max_element = max(arr)
    total_digits = num_digits(max_element)
    place = 1

    for i in range(total_digits): # d(n+k)
        place *= 10
        arr = counting_sort(arr,place)

    return arr

if __name__ == '__main__':
    arr = [564,121,432,421,10,123]
    sorted_arr = radix_sort(arr)
    print(sorted_arr)