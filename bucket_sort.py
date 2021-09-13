def bucket_sort(arr):
    arr_size = len(arr)
    output = [0] * arr_size
    buckets = [[] for i in range(10)]

    for i in arr:
        index = int(10*i)
        buckets[index].append(i)

    for i in range(arr_size):
        buckets[i] = sorted(buckets[i])

    k = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            output[k] = buckets[i][j]
            k += 1

    return output

if __name__ == '__main__':
    arr = [0.64,0.23,0.12,0.47,0.99,0.123,0.999]
    arr = bucket_sort(arr)
    print(arr)